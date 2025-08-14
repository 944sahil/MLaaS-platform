# backend/app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas
from .db.database import SessionLocal, engine

# In a real production app,use a migration tool like Alembic for this.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Synapse MLaaS Platform")

def get_db():
    """
    This is a FastAPI dependency. It's a special function that FastAPI will run
    for every request that needs a database connection. It creates a new database
    session for that single request, yields it for use in the endpoint function,
    and then ensures the session is closed, even if an error occurs.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_sentiment_prediction(text: str) -> dict:
    """
    This is a placeholder for actual ML model.
    """
    if "good" in text.lower() or "great" in text.lower() or "excellent" in text.lower():
        return {"prediction": "Positive", "probability": 0.95}
    elif "bad" in text.lower() or "terrible" in text.lower():
        return {"prediction": "Negative", "probability": 0.95}
    else:
        return {"prediction": "Neutral", "probability": 0.60}


@app.get("/")
def read_root():
    """
    Root endpoint for health checks.
    """
    return {"status": "ok", "message": "Welcome to the Synapse MLaaS Platform!"}


@app.post("/predict", response_model=schemas.PredictionResponse)
def predict(request: schemas.PredictionRequest, db: Session = Depends(get_db)):
    """
    Accepts text input and returns a sentiment prediction.
    """
    prediction_data = get_sentiment_prediction(request.text)
    return schemas.PredictionResponse(**prediction_data)

