from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
import bcrypt
from middleware import create_token, verify_token
from datetime import datetime, timedelta
import jwt

load_dotenv()
app = FastAPI(title="Simple App", version="1.0.0")
class simple(BaseModel):
    name: str  = Field(..., example="Sam Larry")
    email: str  = Field(..., example="sam@example.com")
    password: str  = Field(..., example="sam123")
    userType : str = Field(..., example="student")
    
    token_time = int(os.getenv("token_time"))

@app.post("/signup")
def signup(input: simple):
    try:
        duplicate_query = text("""
            SELECT * FROM users 
            WHERE email = :email
                            """)
        existing = db.execute(duplicate_query, {"email": input.email})
        if existing:
            print("Email already exists")
            #raise HTTPException(status_code=400, detail="Email already exists")

        query = text("""
            INSERT INTO users (name, email, password, userType)
            VALUES (:name, :email, :password, :userType)
        """)
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(input.password.encode("utf-8"), salt)

        db.execute(query, {"name": input.name, "email": input.email, "password": hashed_password, "userType": input.userType})
        db.commit()

        return {"message": "User signed up successfully", 
                "data": {"name": input.name, "email": input.email, "userType": input.userType}}
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
class LoginRequest(BaseModel):
    email:str = Field(..., examples="sam@example.com")
    password: str = Field(..., examples="sam123")
    
# LOGIN ENDPOINT
@app.post("/login")
def login(input: LoginRequest):
    try:
        # Fetch user by email
        query = text("""
        SELECT * FROM users WHERE email = :email
        """)
        
        result = db.execute(query, {"email": input.email}).fetchone()
        
        
        if not result:
            raise HTTPException(status_code=404, detail="Invalid email or password")
    
        # Check password
        verified_password = bcrypt.checkpw(input.password.encode('utf-8'), result.password.encode('utf-8'))
        if not verified_password:
            raise HTTPException(status_code=404, detail="Invalid email or password")
        encoded_token = create_token(details={
            "email":result.email,
            "user_type": result.user_type
            },expiry=token_time)
        return{
        "message": "Login Successful",
        "token": encoded_token
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class courseRequest(BaseModel):
    title: str = Field(..., examples="Backend course")
    level: str = Field(..., examples= "Beginner")
    
@app.post("/courses")
def addcourses(input:courseRequest, user_data = Depends(verify_token)):
    try:
        print(user_data)
        
        
        if user_data['userType'] != 'admin':
            raise HTTPException(status_code=401, detail='You are not authorized to add a course')
        
        query = text("""
            INSERT INTO courses (title, level)
            VALUES (:title, :level)
        """)
        
        db.execute(query, {"title": input.title, "level": input.level})
        db.commit()
        
        return {
            "message": "course added successfully",
            "data": {
                "title": input.title,
                "level": input.level
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__=="__main__":
     uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))