from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    input: str

@app.post("/send")
async def update_list(message: Message):
    msg = message.input

    with open("log.txt", "a") as file:
        file.write(msg+"\n")

    return {"Message": msg}

