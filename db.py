from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

# Create SQLAlchemy engine
connect_args = {}
database_ssl_ca = os.getenv("DATABASE_SSL_CA")
if database_ssl_ca:
    connect_args["ssl"] = {"ca": database_ssl_ca}

engine = create_engine(DATABASE_URL, pool_pre_ping=True, connect_args=connect_args)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()