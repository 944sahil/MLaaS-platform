# backend/app/schemas.py

from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str

class User(BaseModel):
    id: int
    username: str
    email: str
    api_key: str
    is_active: bool

    class Config:
        orm_mode = True

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    probability: float
