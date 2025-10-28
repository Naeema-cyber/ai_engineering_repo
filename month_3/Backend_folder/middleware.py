import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security

bearer = HTTPBearer()

load_dotenv()

secret_key = os.getenv("secret_key")

def create_token(details, expiry: int):
    expire = datetime.now() + timedelta(minutes=expiry)

    details.update({"exp": expire})

    encoded_jwt = jwt.encode(details, secret_key)

    return encoded_jwt

def verify_token(request: HTTPAuthorizationCredentials = Security(bearer)):
    
    token = request.credentials

    verified_token = jwt.decode(token, secret_key, algorithms=["HS256"])

    expiry_time = verified_token.get("exp")

    if datetime.now() > datetime.fromtimestamp(expiry_time):
        raise jwt.ExpiredSignatureError("Token has expired")

    if not verified_token.get("email") or not verified_token.get("usertype"):
        raise jwt.InvalidTokenError("Token is missing required fields")

    return {
        "email": verified_token.get("email"),
        "usertype": verified_token.get("usertype")
    }

    
