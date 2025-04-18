from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import EnergyUsage
from db import SessionLocal
import csv, random
from datetime import datetime

router = APIRouter()

appliances = ["AC", "Heater", "TV", "Microwave"]
rooms = ["Living Room", "Bedroom", "Kitchen"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_entry():
    scenario = random.choice(["normal", "wasteful", "optimal"])
    if scenario == "wasteful":
        appliance = random.choice(["AC", "Heater"])
        hour = random.choice([1, 2, 3])
        duration = random.randint(4, 6)
        label = "Wasteful"
    elif scenario == "optimal":
        appliance = "TV"
        hour = random.choice([19, 20, 21])
        duration = random.randint(1, 2)
        label = "Optimal"
    else:
        appliance = random.choice(appliances)
        hour = random.randint(7, 22)
        duration = random.randint(1, 3)
        label = "Optimal"

    power_usage_kwh = round(duration * random.uniform(0.3, 1.8), 2)
    estimated_cost = round(power_usage_kwh * 6, 2)

    temperature = {
        "AC": random.randint(30, 42),
        "Heater": random.randint(10, 20),
    }.get(appliance, random.randint(20, 35))

    return {
        "timestamp": datetime(2025, 4, 7, hour),
        "appliance": appliance,
        "duration_hrs": duration,
        "room": random.choice(rooms),
        "power_usage_kWh": power_usage_kwh,
        "estimated_cost": estimated_cost,
        "outside_temperature": temperature,
        "label": label
    }

@router.get("/generate-data")
def generate_data(db: Session = Depends(get_db)):
    for _ in range(100):
        data = generate_entry()
        record = EnergyUsage(**data)
        db.add(record)

    db.commit()
    return {"message": "100 records inserted into SQLite database successfully."}
