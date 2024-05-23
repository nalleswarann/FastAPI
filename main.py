from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def name():
    return {"Hello" : "Nalleswaran"}

@app.get("/education/{typeid}")
def education(typeid : int, q : Union[str, None] = None):
    return {'typeid' : typeid, "q" : q}

@app.get("/about")
def show_aboutpage():
    return {'data' : 'about page'}