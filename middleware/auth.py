from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from .config import settings
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def authenticate_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_current_user(request: Request, username: str = Depends(authenticate_user)):
    # You can potentially fetch user information from the database here, using username
    # Example: 
    # user = await database.fetch_user(username)
    # if not user:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return user
    return username

@app.post("/token")
async def generate_token(username: str, password: str):
    # In a production environment, you would fetch the password from a database and use a secure hashing algorithm (e.g., bcrypt) for comparison.
    if username == "admin" and password == "password":
        token = jwt.encode({"sub": username}, settings.JWT_SECRET_KEY, algorithm="HS256")
        return JSONResponse({"access_token": token})
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")