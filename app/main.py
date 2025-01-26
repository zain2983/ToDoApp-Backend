# https://www.youtube.com/watch?v=5GxQ1rLTwaU&t=810s
# https://github.com/techwithtim/Fast-API-Tutorial/blob/main/main.py

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError,jwt
from passlib.context import CryptContext
import random


SECRET_KEY = "55e1dcaca8ce7b2bd7be7a9537a736933c33ea3e80a6b8e174b1072994f9d0be"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30 



sepr = "="*40 

fake_db = {
    "tim" : {
        "username":"",
        "full_name":"Tim Rusna",
        "email":"timmy444@gmail.com",
        "hashed_password":"",
        "disabled":False,
    }
}


class Token(BaseModel):
    access_token : str
    token_type : str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password : str


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")



app = FastAPI()


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db,username:str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)

def authenticate_user(db,username:str,password:str):
    user = get_user(db,username)
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY , algorithm=ALGORITHM)
    return encoded_jwt




# class Data(BaseModel):
#     name:str


# @app.post("/create/")
# async def create(data:Data):
#     return {"data":data}


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI server!"}


# @app.get("/random")
# async def read_rand1():
#     random_number = random.randint(1, 100)
#     msg = {"msg":random_number}
#     print(sepr,"Sent : ", random_number,sepr)
#     return msg
#     # return {"message": "Welcome to the FastAPI server!"}