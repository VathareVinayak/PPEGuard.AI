# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from models.database import get_db
# from models.user import User
# from services.auth_services import verify_password, create_access_token
# from pydantic import BaseModel

# user_router = APIRouter(prefix="/users", tags=["Users"])

# # Pydantic model for request validation
# class UserLogin(BaseModel):
#     email: str
#     password: str

# # Login and generate JWT token
# @user_router.post("/login")
# def login_user(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

#     access_token = create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}


# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from models.database import get_db
# from models.user import User
# from services.auth_services import verify_password, create_access_token
# from pydantic import BaseModel

# user_router = APIRouter(prefix="/users", tags=["Users"])

# # Pydantic model for request validation
# class UserLogin(BaseModel):
#     email: str
#     password: str

# # Login and generate JWT token
# @user_router.post("/login")
# def login_user(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

#     # Include the user role in the token payload
#     access_token = create_access_token(data={"sub": user.email, "role": db_user.role})

#     return {
#         "access_token": access_token,
#         "token_type": "bearer",
#         "role": db_user.role  # Include user role in response
#     }



from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.database import get_db
from models.user import User
from services.auth_services import verify_password, create_access_token
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from main import app  # Import app to apply CORS

user_router = APIRouter(prefix="/users", tags=["Users"])

# Enable CORS to allow frontend requests
origins = ["*"]  # Allow all origins; restrict in production if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request validation
class UserLogin(BaseModel):
    email: str
    password: str

# Login and generate JWT token
@user_router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Include user role in token payload
    access_token = create_access_token(data={"sub": user.email, "role": db_user.role})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": db_user.role  # Include user role in response
    }
