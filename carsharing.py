from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    """Return a friendly welcome message."""
    return {'message': "Welcome to the Car Sharing service!"}

@app.get("/date")
def welcome():
    """Return the date."""
    return {'date': datetime.now()}
