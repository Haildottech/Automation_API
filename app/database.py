from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.automap import automap_base

SQL_ALCHEMY_URL = "cockroachdb://saim:R2_RkmUt3xc59Gjzuhn33A@joking-egret-7111.8nk.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"

engine = create_engine(SQL_ALCHEMY_URL)



sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

baseclass = declarative_base()


metadata = MetaData()
from sqlalchemy import Table, MetaData

Base = automap_base(metadata=metadata)
Base.prepare()

# Access the mapped classes
Table1 = print(dir(Base))
# Table2 = Base.classes.DMC_success_records

metadata = MetaData()

# Reflect each table separately
table1 = Table('DMC_failed_records', metadata, autoload_with=engine)
table2 = Table('DMC_success_records', metadata, autoload_with=engine)

print(table1.columns)
# ... (do this for each table you need)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()