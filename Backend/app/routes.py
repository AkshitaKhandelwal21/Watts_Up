from fastapi import APIRouter
import csv
import random
from datetime import datetime

router = APIRouter()

appliances = ["AC", "Heater", "TV", "Microwave"]
rooms = ["Living Room", "Bedroom", "Kitchen"]

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

    if appliance == "AC":
        temperature = random.randint(30, 42)
    elif appliance == "Heater":
        temperature = random.randint(10, 20)
    else:
        temperature = random.randint(20, 35)

    return {
        "timestamp": f"2025-04-07 {hour}:00",
        "appliance": appliance,
        "duration_hrs": duration,
        "room": random.choice(rooms),
        "power_usage_kWh": power_usage_kwh,
        "estimated_cost": estimated_cost,
        "outside_temperature": temperature,
        "label": label
    }

@router.get("/generate-data")
def generate_data():
    filename = "mock_energy_data.csv"
    fieldnames = [
        "timestamp", "appliance", "duration_hrs", "room",
        "power_usage_kWh", "estimated_cost", "outside_temperature", "label"
    ]

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(100):
            writer.writerow(generate_entry())

    return {"message": f"{filename} generated successfully with 100 records."}
