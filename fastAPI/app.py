from fastapi import FastAPI,Path,HTTPException,Query
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

@app.get('/patients/{patients_id}')
def patients(patients_id:str = Path(...,description="id of the patients in the DB",example="P001")):
    data=load_data()
    if patients_id in data:
        return data[patients_id]
    raise HTTPException(status_code=404,detail='patient not found in data base')

@app.get('/sort')
def sort_patients(sort_by:str = Query(...,description='sort in the basis of height, weight or bmi'), order:str = Query('acending',description='sort acending ort decending order')):
    valid_fields=['weight','height','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'invalid fields, select from{valid_fields}')
    if order not in ['acending','decending']:
        raise HTTPException(status_code=400,detail='invalide order select between acending or decending')
    data=load_data()

    sort_order=True if order=='decending' else False

    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data
