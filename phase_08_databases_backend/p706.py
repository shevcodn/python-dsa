from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

fake_db = {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}

def get_db():
    return fake_db

@app.get("/users")
async def get_users(db: dict = Depends(get_db)):
    return db["users"]

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: dict = Depends(get_db)):
    user = next((u for u in db["users"] if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_user(user_id: int = 1, db: dict = Depends(get_db)):
    user = next((u for u in db["users"] if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/me")
async def read_current_user(user: dict = Depends(get_current_user)):
    return user