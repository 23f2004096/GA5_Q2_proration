from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ProrationRequest(BaseModel):
    old_price: float
    new_price: float
    days_remaining: float
    days_in_actual_month: float
    spec: str


@app.post("/")
def calculate_charge(data: ProrationRequest):

    difference = data.new_price - data.old_price

    if data.spec == "v1":
        charge = difference * (data.days_remaining / 30)

    elif data.spec == "v2":
        charge = difference * (
            data.days_remaining /
            data.days_in_actual_month
        )

    else:
        charge = 0

    return {
        "charge": charge
    }