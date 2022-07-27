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


@app.get("/")
async def belzinha():
    curiosidades = [
        "Roberta gosta muito de dormir e dorme em qualquer lugar. Eu tenho dificuldade pra pegar no sono",
        "Nós gostamos muito de azul!",
        "Roberta tem uma agendinha azul",
        "Mateus já deu um buquê de rosas pintadas de Azul para Roberta",
        "Uma vez Roberta ganhou uma camisa azul enorme de um congresso, se deu o apelido de balão azul",
        "Nosso primeiro encontro foi no cinema!",
        "Cantor favorito em comum, Ed Sheeran. Inclusive, ouçam The Joker and the Queen.",
        "Amamos Café! Eu sempre uso ela de cobaia perguntando se o café ainda está quente demais :3",
        "Ela é a dentista mais pezinho pra dentro de TI que eu já vi na vida. Um dia ainda puxo ela",
        "Houve um tempo no relacionamento que eu contava historinhas completas pra botar ela pra dormir.",
        "Nós já passamos altas tardes lado a lado jogando league of legends",
        "Todo ano trocamos livros de presentes",
        "Ela me pediu em namoro na praia em Maceió",
        "Estivemos desde sempre muito conectados. Escrevi um soneto pra ela 3 semanas atrás, ontem, ela me 'citou' 1 estrofe dele. É autoral.",
        "Zeramos Resident Evil 7 em 1 dia. Começamos de manhã cedo e ficamos até de madrugada kkkk",
        "Eu já sabia que ia casar com ela há cerca de 5 anos atrás, e mesmo assim a certeza parece que só aumenta a cada dia.",
        "Começamos a namorar no dia 18/07/2016",
        "Na época da faculdade vínhamos pra casa e ela deitava e literalmente dormia",
        "Sempre que pensamos em ir pra Maceió acontece alguma coisa interessante na nossa vida. Alguém engravida, alguém casa, etc.",
        "Ela entende muito de investimento!",
        "Esse ano ela fez meu Imposto de Renda, me rendeu um bom lucro, que já está voltando para ela rs",
    ]
    return {
        "statusCode":200,
        "curiosidade":random.choice(curiosidades)
    }
    
