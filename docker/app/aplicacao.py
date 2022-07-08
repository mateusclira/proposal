from fastapi import  FastAPI
from flask import Flask
from flask_cors import CORS
import random 
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


app  = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {
        "statusCode":200,
        "message":"OK"
    }


@app.get("/belzinha")
async def belzinha():
    curiosidades = [
        "Belzinha gosta muito de dormir e dorme em qualquer lugar",
        "Belzinha gosta muito de azul! Eu também"
    ]
    return {
        "statusCode":200,
        "curiosidade":random.choice(curiosidades)
    }