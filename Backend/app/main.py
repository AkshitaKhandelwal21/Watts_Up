from fastapi import FastAPI
import routes
from models import Base
from db import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(routes.router)
