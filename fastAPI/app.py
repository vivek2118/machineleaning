from fastapi import FastAPI
import json

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data

@app.get('/')
def hello():
    return{'message':'patiante management system API'}

@app.get('/about')
def about():
    return{'message':'a fully functional API tto manage your patiante records'}


@app.get('/view')
def view():
    data=load_data()
    return data

