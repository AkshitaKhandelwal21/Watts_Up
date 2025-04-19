from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from app.routes import router
from app.dataframe import data
from app.dashboard import dashboard
from app.kpi import kpi
from app.apply_label import label_router
from app.models import Base
from app.db import engine
from llm_model.llm_routes import LLMrouter
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
# templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(data)
app.include_router(label_router)
app.include_router(dashboard)
app.include_router(kpi)
app.include_router(LLMrouter)