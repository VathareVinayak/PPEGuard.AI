# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # Dependency for DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# backend/models/database.py
# backend/models/database.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # Base model for SQLAlchemy
from sqlalchemy.orm import sessionmaker

# Load .env file (looks in current directory first)
load_dotenv()

# Get DB URL from environment (.env must contain DATABASE_URL)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set. Please check your .env file.")

# Create SQLAlchemy engine (this connects to your DB)
engine = create_engine(DATABASE_URL)

# Create DB session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models (used for table creation)
Base = declarative_base()

# Dependency for DB session (used inside FastAPI routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
