from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.automap import automap_base

SQL_ALCHEMY_URL = "cockroachdb://saim:R2_RkmUt3xc59Gjzuhn33A@joking-egret-7111.8nk.cockroachlabs.cloud:26257/defaultdb?sslmode=require"

engine = create_engine(SQL_ALCHEMY_URL)
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