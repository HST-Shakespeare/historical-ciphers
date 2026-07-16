from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/ciphers")
def get_ciphers():
    return {"ciphers": ["Caesar", "Vigenère", "Rail Fence"]}

@app.get("/encrypt/{message}")
def encrypt_message(message: str):
    return message