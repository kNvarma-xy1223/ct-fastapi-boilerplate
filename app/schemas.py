from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    name: str
    age: int = Field(gt=0, lt=120)
    email: EmailStr


class ChatRequest(BaseModel):
    message: str
