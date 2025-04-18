from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EnergyUsage(Base):
    __tablename__ = "energy_usage"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    appliance = Column(String)
    duration_hrs = Column(Integer)
    room = Column(String)
    power_usage_kWh = Column(Float)
    estimated_cost = Column(Float)
    outside_temperature = Column(Integer)
    label = Column(String)
