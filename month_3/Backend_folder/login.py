from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
import bcrypt

from month_3 import app

class LoginRequest(BaseModel):
    email: str = Field(..., example="sam@example.com")
    password: str = Field(..., example="sam123")


@app.post("/login")
def login(input: LoginRequest ):
    try:
       query = text("""
        SELECT * FROM users WHERE email = :email
""")
       result = db.execute(query, {"email": input.email}).fetchone()

       if not result:
           raise HTTPException(status_code=401, detail = "invalid email or password")
       
       verified_password = bcrypt.checkpw(input.password.encode('utf-8'), result.password.encode('utf-8'))

        if not verified_password:
           raise HTTPException(status_code=404, detail="invalid email or password")
       return {
           "message": "Login Successful"
        }
   except Exception as e:
         raise HTTPException(status_code=500, detail=str(e))