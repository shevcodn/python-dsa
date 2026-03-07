import asyncio
import httpx
import aiofiles
import json
from rich.console import Console
from rich.table import Table


class StockClient:
    BASE_URL = "https://query1.finance.yahoo.com"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    def __init__(self):
        self.client = None
        self.portfolio = {}
        self.alerts = {}

    async def __aenter__(self):
        self.client = httpx.AsyncClient(base_url=self.BASE_URL, headers=self.HEADERS)
        return self
    
    async def __aexit__(self, *args):
        await self.client.aclose()
        self.client = None

    async def get_price(self, ticker) -> float:
        try:
            response = await self.client.get(f"/v8/finance/chart/{ticker}", timeout=5.0)
            response.raise_for_status()
            return float(response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"])
        except (httpx.HTTPError, KeyError, IndexError):
            print(f"Error fetching price for {ticker}")
            return None
        
    async def get_prices(self, tickers) -> dict:
        try:
            response = await self.client.get(f"/v7/finance/quote?symbols={','.join(tickers)}", timeout=5.0)
            response.raise_for_status()
            return float(response.json()["quoteResponse"]["result"][0]["regularMarketPrice"])
        except (httpx.HTTPError, KeyError, IndexError):
            print(f"Error fetching {ticker}: {e}")
            return None
    
    async def add_position(self, ticker, shares, avg_price):
        self.portfolio[ticker] = {"shares": shares, "avg_price": avg_price}
        
    async def get_portfolio_value(self) -> dict:
        result = {}
        total = 0.0
        for ticker, pos in self.portfolio.items():
            current = await self.get_price(ticker)
            if current is None:
                continue
            value = pos["shares"] * current
            pnl = (current - pos["avg_price"]) * pos["shares"]
            result[ticker] = {"shares": pos["shares"], "current": current, "value": round(value, 2), "pnl": round(pnl, 2)}
            total += value
        result["TOTAL"] = round(total, 2)
        return result
    
    async def add_alert(self, ticker, above=None, below=None):
        self.alerts[ticker] = {"above": above, "below": below}

    async def check_alerts(self):
        for ticker, alert in self.alerts.items():
            current = await self.get_price(ticker)
            if alert["above"] is not None and current > alert["above"]:
                print(f"ALERT: {ticker} ABOVE ${alert['above']} | current: ${current}")
            if alert["below"] is not None and current < alert["below"]:
                print(f"ALERT: {ticker} BELOW ${alert['below']} | current: ${current}")

    async def save_portfolio(self, filename):
        async with aiofiles.open(filename, "w") as f:
            await f.write(json.dumps(self.portfolio, indent=2))

    async def load_portfolio(self, filename):
        async with aiofiles.open(filename, "r") as f:
            content = await f.read()
            self.portfolio = json.loads(content)

    async def print_portfolio(self, portfolio):
        console = Console()
        table = Table()
        table.add_column("Ticker")
        table.add_column("Shares")
        table.add_column("Current")
        table.add_column("Value")
        table.add_column("PnL")
        for ticker, data in portfolio.items():
            if ticker == "TOTAL":
                continue
            pnl = data['pnl']
            pnl_str = f"[green]${pnl}[/green]" if pnl > 0 else f"[red]${pnl}[/red]"
            table.add_row(ticker, str(data["shares"]), f"${data['current']}", f"${data['value']}", pnl_str)
        console.print(table)
        print(f"\nTotal value: ${portfolio['TOTAL']}")

    async def monitor(self, interval=10):
        while True:
            portfolio = await self.get_portfolio_value()
            await self.print_portfolio(portfolio)
            await self.check_alerts()
            await asyncio.sleep(interval)



async def main():
    async with StockClient() as client:
        while True:
            print("\n1. Add position\n2. Show portfolio\n3. Add alert\n4. Check alerts\n5. Save\n6. Exit")
            choice = input("Choice: ")
            if choice == "1":
                ticker = input("Ticker: ")
                shares = int(input("Shares: "))
                avg_price = float(input("Avg price: "))
                await client.add_position(ticker, shares, avg_price)
            elif choice == "2":
                portfolio = await client.get_portfolio_value()
                await client.print_portfolio(portfolio)
            elif choice == "3":
                ticker = input("Ticker: ")
                above = input("Alert above (or leave empty): ")
                below = input("Alert below (or leave empty): ")
                above_val = float(above) if above else None
                below_val = float(below) if below else None
                await client.add_alert(ticker, above=above_val, below=below_val)
            elif choice == "4":
                await client.check_alerts()
            elif choice == "5":
                filename = input("Filename: ")
                await client.save_portfolio(filename)
                print("Saved.")
            elif choice == "6":
                print("Exiting.")
                break
            elif choice == "7":
                ticker = input("Ticker: ").upper()
                price = await client.get_price(ticker)
                if price is None:
                    print(f"{ticker} failed to fetch price")
                else:
                    print(f"{ticker}: ${price}")

if __name__ == "__main__":
    asyncio.run(main())