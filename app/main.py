from fastapi import FastAPI,Depends,HTTPException
from .database import sessionLocal,engine,get_db,table1,table2,table3
from sqlalchemy.orm import Session
import json

app = FastAPI()

with open(r"database.json",'r') as database:
    database_cred = json.load(database)


@app.get("/")
def root():
    return {"message":"Hello world"}

@app.get("/damco-success")
def get_dmc_scs_rec(db: Session = Depends(get_db)):
    result = db.query(table2).all()
    # print(type(result),result)
    serialized_results = [dict(row._asdict()) for row in result]
    # serialized_results = [dict(row) for row in result]
    # print(serialized_results)
    return {"message" : serialized_results}

@app.get("/nxs-success")
def get_nxs_scs_rec(db: Session = Depends(get_db)):
    result = db.query(table3).all()
    # print(type(result),result)
    serialized_results = [dict(row._asdict()) for row in result]
    # serialized_results = [dict(row) for row in result]
    # print(serialized_results)
    return {"message" : serialized_results}