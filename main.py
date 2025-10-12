from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def welcome():
    return "hello world"

@app.get('/greet/{name}')
def greet(name:str):
    return f'hello {name} welcome to fast api'
