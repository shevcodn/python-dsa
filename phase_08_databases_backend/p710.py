from jose import jwt
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        return None
    
@app.post("/token")
async def login():
    user_data = {"sub": "user1"}
    token = create_token(user_data)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
async def read_current_user(token: str):
    payload = decode_token(token)
    if payload is None:
        return {"error": "Invalid token"}
    return {"user": payload["sub"]}

