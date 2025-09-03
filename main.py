# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# O Pydantic ajuda a validar os dados que chegam na sua API.
# Aqui, estamos dizendo que esperamos um JSON com um campo "username".
class UserRequest(BaseModel):
    username: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "API está no ar!"}

# Este é o endpoint que você pediu!
@app.post("/auth/me")
def auth_me(user_request: UserRequest):
    # A mágica acontece aqui: pegamos o username do corpo da requisição
    # e montamos o JSON de resposta.
    return {
        "user": user_request.username,
        "ping": "pong"
    }