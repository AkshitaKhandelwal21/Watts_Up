from fastapi import APIRouter
from sqlalchemy.orm import Session
from db import SessionLocal
from models import EnergyUsage
import pandas as pd
from collections import defaultdict

dashboard = APIRouter()

def get_df():
    session: Session = SessionLocal()
    data = session.query(EnergyUsage).all()
    df = pd.DataFrame([d.__dict__ for d in data])
    df.drop("_sa_instance_state", axis=1, inplace=True)
    return df

@dashboard.get("/charts")
def get_chart_data():
    df = get_df()

    charts = {}

    # 1. Appliance-wise Power Usage and Cost breakdown
    appliance_group = df.groupby("appliance").agg({"power_usage_kWh": "sum", "estimated_cost": "sum"}).reset_index()
    charts["appliance_power_cost"] = {
        "appliances": appliance_group["appliance"].tolist(),
        "power_usage": appliance_group["power_usage_kWh"].tolist(),
        "costs": appliance_group["estimated_cost"].tolist()
    }

    # 2. Time-of-Day Usage Pattern
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    hourly = df.groupby("hour")["power_usage_kWh"].sum().reset_index()
    charts["time_of_day"] = {
        "hours": hourly["hour"].tolist(),
        "usage": hourly["power_usage_kWh"].tolist()
    }

    # 3. Room-wise Consumption
    room_group = df.groupby("room")["power_usage_kWh"].sum().reset_index()
    charts["room_consumption"] = {
        "rooms": room_group["room"].tolist(),
        "usage": room_group["power_usage_kWh"].tolist()
    }

    # 4. Appliances by Label
    label_group = df.groupby(["appliance", "label"]).size().unstack(fill_value=0)
    charts["appliance_label"] = {
        "appliances": label_group.index.tolist(),
        "labels": label_group.columns.tolist(),
        "counts": label_group.to_dict(orient="list")
    }

    # 5. Monthly Heatmap (using day instead for now)
    df["day"] = pd.to_datetime(df["timestamp"]).dt.day
    heatmap = df.groupby(["day", "hour"])["power_usage_kWh"].sum().unstack(fill_value=0)
    charts["heatmap"] = {
        "days": heatmap.index.tolist(),
        "hours": heatmap.columns.tolist(),
        "data": heatmap.values.tolist()
    }

    return charts
