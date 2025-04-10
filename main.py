from fastapi import FastAPI
from pydantic import BaseModel
import chat
class Post(BaseModel):
    user: str

app = FastAPI()

@app.get("/")
async def root():
    return {"msg":"Hello World"}

@app.post("/chat")
async def genAi(new_chat: Post):
    respone = chat.chat(new_chat.user)
    return respone
