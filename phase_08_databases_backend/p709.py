import os
import asyncpg
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException, Depends
from pydantic import BaseModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.pool = await asyncpg.create_pool(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )
    async with app.state.pool.acquire() as conn:
        await conn.execute("DROP TABLE IF EXISTS notes")
        await conn.execute("""
            CREATE TABLE notes (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """)
    yield
    await app.state.pool.close()

app = FastAPI(lifespan=lifespan)

async def get_db(request: Request):
    async with request.app.state.pool.acquire() as conn:
        yield conn

class NoteIn(BaseModel):
    title: str
    content: str

@app.get("/notes")
async def get_notes(conn=Depends(get_db)):
    rows = await conn.fetch("SELECT * FROM notes")
    return [dict(r) for r in rows]

@app.post("/notes", status_code=201)
async def create_note(note: NoteIn, conn=Depends(get_db)):
    row = await conn.fetchrow(
        "INSERT INTO notes (title, content) VALUES ($1, $2) RETURNING *",
        note.title, note.content
    )
    return dict(row)

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int, conn=Depends(get_db)):
    row = await conn.fetchrow("SELECT id FROM notes WHERE id = $1", note_id)
    if not row:
        raise HTTPException(status_code=404, detail="Note not found")
    await conn.execute("DELETE FROM notes WHERE id = $1", note_id)
    return {"message": "deleted"}
