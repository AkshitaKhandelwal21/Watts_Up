from sqlalchemy import inspect
from models import EnergyUsage
from db import SessionLocal
from fastapi.responses import JSONResponse
from fastapi import APIRouter
import pandas as pd

data = APIRouter()

@data.get("/dataframe")
def fetch_data():
    session = SessionLocal()
    try:
        mapper = inspect(EnergyUsage)
        columns = [column.key for column in mapper.attrs]
        users = session.query(EnergyUsage).all()

        output = [{column: getattr(user, column) for column in columns} for user in users]
        df = pd.DataFrame(output)
        df["timestamp"] = df["timestamp"].astype(str)
        return JSONResponse(content=df.to_dict(orient="records"))
    except Exception as e:
        print(f"Error fetching data: {e}")
        return JSONResponse(content={"error": "Failed to fetch data."})
    
