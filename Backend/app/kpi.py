
from dashboard import get_df
from fastapi import APIRouter

kpi = APIRouter()


@kpi.get("/kpi")
def get_kpi_data():
    df = get_df()

    most_used_appliance = df.groupby("appliance")["duration_hrs"].sum().idxmax()
    top_duration = df.loc[df["duration_hrs"].idxmax(), "duration_hrs"]
    most_used_room = df["room"].mode()[0]
    total_cost = round(df["estimated_cost"].sum(), 2)

    return {
        "most_used_appliance": most_used_appliance,
        "longest_duration": top_duration,
        "most_used_room": most_used_room,
        "total_cost": total_cost
    }
