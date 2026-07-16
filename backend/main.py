from fastapi import FastAPI
from pydantic import BaseModel
from ciphers import caesar

class EncryptRequest(BaseModel):
    cipher: str
    message: str
    key: str | int

cipher_modules = {
    "caesar": caesar
}

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/ciphers")
def get_ciphers():
    return {"ciphers": ["caesar"]}

@app.post("/encrypt")
def encrypt(data: EncryptRequest):
    module = cipher_modules[data.cipher]
    result = module.encrypt(data.message, data.key)

    return {
        "result": result
    }