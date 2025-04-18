from fastapi import FastAPI
from routes import router
from dataframe import data
from dashboard import dashboard
from kpi import kpi
from models import Base
from db import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(data)
app.include_router(dashboard)
app.include_router(kpi)