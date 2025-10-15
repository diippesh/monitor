from fastapi import FastAPI
import app_insights_logger

app = FastAPI()

@app.get('/')
def welcome():
    return "hello worldd"

@app.get('/greet/{name}')
def greet(name:str):
    return f'hello {name} welcome to fast api'
