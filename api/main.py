from fastapi import FastAPI
from pydantic import BaseModel
from .chat_module import chat
from fastapi.middleware.cors import CORSMiddleware


class Post(BaseModel):
    user: str

app = FastAPI()

origins = [
    "http://localhost:5173",  # your React app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],     # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # allow all headers
)

@app.get("/")
async def root():
    return {"msg":"Hello World"}

@app.post("/chat")
async def genAi(new_chat: Post):
    # Call the imported 'chat' function directly
    # Also fix the typo 'respone' -> 'response'
    response = chat(new_chat.user) 
    return response
