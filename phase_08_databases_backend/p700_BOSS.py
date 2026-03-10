import asyncio
import asyncpg

def create_pool():
    return asyncpg.create_pool(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777",
        min_size=1, max_size=5
    )

async def create_account(pool, owner, balance):
    async with pool.acquire() as conn:
        return await conn.fetchrow("INSERT INTO bank_accounts (owner, balance) VALUES ($1, $2) RETURNING id", owner, balance)

async def transfer(pool, from_id, to_id, amount):
    async with pool.acquire() as conn:
        try:
            await conn.execute("SELECT transfer_funds($1, $2, $3)", from_id, to_id, amount)
            print(f"Transfer {amount} success")
        except Exception as e:
            print(f"Transfer {amount} failed: {e}")

async def get_summary(pool):
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT owner, balance, RANK() OVER (ORDER BY balance DESC) as rank FROM bank_accounts")

async def main():
    pool = await create_pool()

    async with pool.acquire() as conn:
        await conn.execute("DROP TABLE IF EXISTS transaction_log")
        await conn.execute("DROP TABLE IF EXISTS bank_accounts")
        await conn.execute("""
            CREATE TABLE bank_accounts (
                id SERIAL PRIMARY KEY,
                owner TEXT NOT NULL,
                balance REAL NOT NULL CHECK (balance >= 0),
                created_at TIMESTAMP DEFAULT NOW(),
                updated_at TIMESTAMP DEFAULT NOW()
            )
        """)
        await conn.execute("""
            CREATE TABLE transaction_log (
                id SERIAL PRIMARY KEY,
                from_account INTEGER REFERENCES bank_accounts(id) ON DELETE SET NULL,
                to_account INTEGER REFERENCES bank_accounts(id) ON DELETE SET NULL,
                amount REAL NOT NULL CHECK (amount > 0),
                status TEXT NOT NULL CHECK (status IN ('pending', 'completed', 'failed')),
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        await conn.execute("""
            CREATE OR REPLACE FUNCTION transfer_funds(from_account_id INTEGER, to_account_id INTEGER, amount REAL) RETURNS VOID AS $$
            DECLARE
                from_balance REAL;
            BEGIN
                SELECT balance INTO from_balance FROM bank_accounts WHERE id = from_account_id FOR UPDATE;
                IF from_balance < amount THEN
                    INSERT INTO transaction_log (from_account, to_account, amount, status) VALUES (from_account_id, to_account_id, amount, 'failed');
                    RAISE EXCEPTION 'Insufficient funds';
                END IF;
                UPDATE bank_accounts SET balance = balance - amount, updated_at = NOW() WHERE id = from_account_id;
                UPDATE bank_accounts SET balance = balance + amount, updated_at = NOW() WHERE id = to_account_id;
                INSERT INTO transaction_log (from_account, to_account, amount, status) VALUES (from_account_id, to_account_id, amount, 'completed');
            END;
            $$ LANGUAGE plpgsql
        """)

    alice = await create_account(pool, "Alice", 1000.0)
    bob = await create_account(pool, "Bob", 500.0)
    carol = await create_account(pool, "Carol", 200.0)

    await transfer(pool, alice["id"], bob["id"], 300.0)
    await transfer(pool, bob["id"], carol["id"], 1000.0)
    await transfer(pool, carol["id"], alice["id"], 50.0)

    summary = await get_summary(pool)
    print("\nAccount summary:")
    for record in summary:
        print(f"  Rank {record['rank']}: {record['owner']} — ${record['balance']}")

    async with pool.acquire() as conn:
        logs = await conn.fetch("SELECT * FROM transaction_log")
    print("\nTransaction log:")
    for log in logs:
        print(f"  {log['status'].upper()}: ${log['amount']} from {log['from_account']} to {log['to_account']}")

    await pool.close()

if __name__ == "__main__":
    asyncio.run(main())