
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {"alice": {"username": "alice", "hashed_password": pwd_context.hash("secret")}}

async def create_token(username: str, expires_minutes: int = 15):
    to_encode = {"sub": username}
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.exceptions.InvalidTokenError:      
        raise HTTPException(status_code=401, detail="Invalid token")
    
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = await create_token(user["username"], expires_minutes=15)
    refresh_token = await create_token(user["username"], expires_minutes=10080)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@app.post("/refresh")
async def refresh(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        new_access = await create_token(username, expires_minutes=15)
        return {"access_token": new_access, "token_type": "bearer"}
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

@app.get("/me")
async def read_current_user(username: str = Depends(get_current_user)):
    return {"username": username}