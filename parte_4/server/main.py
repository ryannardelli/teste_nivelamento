# Aqui estou importando o Flask que será usado para criar a api
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}