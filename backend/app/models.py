# backend/app/models.py

from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from .db.database import Base 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    api_key = Column(String, unique=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    # This creates the relationship to the MLModel table
    models = relationship("MLModel", back_populates="owner")

class MLModel(Base):
    __tablename__ = "ml_models"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, nullable=False)
    model_version = Column(String, nullable=False)
    description = Column(String, nullable=True)
    s3_path = Column(String, nullable=False)
    input_schema = Column(JSON, nullable=True)
    output_schema = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    # This creates the reverse relationship back to the User table
    owner = relationship("User", back_populates="models")
