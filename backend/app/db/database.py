# backend/app/db/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# "postgresql://user:password@host:port/database_name"
SQLALCHEMY_DATABASE_URL = "postgresql://synapse_user:synapse_password@localhost:5432/synapse_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
