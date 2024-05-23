from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI()

# @app.get("/")
# def name():
#     return {"Hello" : "Nalleswaran"}

# @app.get("/education/{typeid}")
# def education(typeid : int, q : Union[str, None] = None):
#     return {'typeid' : typeid, "q" : q}

# @app.get("/about")
# def show_aboutpage():
#     return {'data' : 'about page'}


#--------------------------------------------------------------------

#CRUD Operation

class BankCustomer(BaseModel):
    cus_id: int
    cus_name: str
    cus_loginName: str
    cus_pass: str
    cus_status: str

customers: List[BankCustomer] = []

@app.get('/customers')
def show_customers():
    return customers

# @app.get('/customers/{cus_id}')
# def show_customer(cus_id : int):
#    return {cus_id}

@app.post('/customer')
def create_customer(customer: BankCustomer):
    customers.append(customer)
    return customer

@app.put('/customer/{cus_id}')
def update_customer(cus_id: int, update_customer: BankCustomer):
    for index, customer in enumerate(customers):
        if customer.cus_id == cus_id:
            customers[index] = update_customer
            return customers
    raise HTTPException(status_code=404, detail=f"Customer with id {cus_id} not found, so can't ablt to update")

@app.delete('/customer/{cus_id}')
def delete_customer(cus_id: int):
  global customers
  for index, customer in enumerate(customers):
    if customer.cus_id == cus_id:
      del customers[index]
      return customers
  raise HTTPException(status_code=404, detail=f"Customer with id {cus_id} not found, so can't able to delete")
