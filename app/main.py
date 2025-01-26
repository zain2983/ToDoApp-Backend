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


app = FastAPI()
sepr = "="*40 

fake_db = {
    
}



















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
