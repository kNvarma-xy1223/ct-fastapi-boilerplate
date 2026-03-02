from fastapi import FastAPI
from app.schemas import User

app = FastAPI()


@app.get("/")
def root():
    return {"message": "CT Cognitive Tech API Running"}


@app.post("/user")
def create_user(user: User):
    return {"message": "User created successfully", "data": user}
