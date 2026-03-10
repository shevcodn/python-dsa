from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from fastapi import Depends, FastAPI, HTTPException, status


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {"alice": {"username": "alice", "hashed_password": pwd_context.hash("secret")}}

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    return {"access_token": "some_token", "token_type": "bearer"}

@app.get("/me")
async def read_current_user(token: str = Depends(oauth2_scheme)):
    if token != "some_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "alice"}


