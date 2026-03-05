from fastapi import FastAPI
from app.schemas import User
import httpx
import json
from fastapi.responses import StreamingResponse
from app.schemas import ChatRequest
from app.config import settings


app = FastAPI()

LM_STUDIO_URL = settings.lm_studio_url


async def stream_llm(message: str):
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream(
            "POST",
            LM_STUDIO_URL,
            json={
                "model": settings.lm_model,
                "messages": [{"role": "user", "content": message}],
                "stream": True,
            },
        ) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data = line.replace("data: ", "")

                    if data == "[DONE]":
                        break

                    try:
                        chunk = json.loads(data)
                        content = chunk["choices"][0]["delta"].get("content", "")
                        if content:
                            yield content
                    except Exception:
                        pass


@app.get("/")
def root():
    return {"message": "CT Cognitive Tech API Running"}


@app.post("/user")
def create_user(user: User):
    return {"message": "User created successfully", "data": user}


@app.post("/chat")
async def chat(request: ChatRequest):
    return StreamingResponse(stream_llm(request.message), media_type="text/plain")
