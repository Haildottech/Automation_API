from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.automap import automap_base
import json

with open(r"database.json",'r') as database:
    database_cred = json.load(database)

engine = create_engine(database_cred['database_url'])
sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
metadata = MetaData()

baseclass = declarative_base()

# Reflect each table separately
table1 = Table('DMC_failed_records', metadata, autoload_with=engine)
table2 = Table('DMC_success_records', metadata, autoload_with=engine)
table3 = Table('nxs_success_records', metadata, autoload_with=engine)
print(table1.columns)
print(table3.columns)

# ... (do this for each table you need)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()