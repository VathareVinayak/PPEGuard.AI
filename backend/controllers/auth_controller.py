# from fastapi import APIRouter, Depends, HTTPException, status
# from jose import JWTError, jwt
# import os
# from dotenv import load_dotenv

# load_dotenv()

# SECRET_KEY = os.getenv("SECRET_KEY")
# ALGORITHM = "HS256"

# auth_router = APIRouter(prefix="/auth", tags=["Auth"])  # Fix: Change `user_router` to `auth_router`

# def get_current_user(token: str = Depends(lambda token: token)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
#         return email
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# @auth_router.get("/me")
# def get_user_info(current_user: str = Depends(get_current_user)):
#     return {"email": current_user}


# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# SECRET_KEY = os.getenv("SECRET_KEY")
# ALGORITHM = "HS256"

# # OAuth2 for extracting token from Authorization header
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# auth_router = APIRouter(prefix="/auth", tags=["Auth"])

# # Function to extract user from JWT token
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
#         return email
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# # Endpoint to get user info
# @auth_router.get("/me")
# def get_user_info(current_user: str = Depends(get_current_user)):
#     return {"email": current_user}


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

# Define HTTPBearer scheme
bearer_scheme = HTTPBearer()

# Function to extract user from JWT token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials  # Extract token from Authorization header
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
        return email
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# Endpoint to get user info
@auth_router.get("/me")
def get_user_info(current_user: str = Depends(get_current_user)):
    return {"email": current_user}
