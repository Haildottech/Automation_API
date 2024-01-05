from fastapi import FastAPI,Depends,HTTPException
from .database import sessionLocal,engine,get_db,table1,table2
from sqlalchemy.orm import Session

app = FastAPI()



@app.get("/")
def root():
    return {"message":"Hello world"}

@app.get("/damco-failed")
def get_dmc_fld_rec(db: Session = Depends(get_db)):
    result = db.query(table2).all()
    return {"data" : result}
