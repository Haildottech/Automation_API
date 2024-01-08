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
    # print(type(result),result)
    serialized_results = [dict(row._asdict()) for row in result]
    # serialized_results = [dict(row) for row in result]
    # print(serialized_results)
    return {"message" : serialized_results}
