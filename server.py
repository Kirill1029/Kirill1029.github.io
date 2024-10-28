import re

from fastapi import FastAPI, HTTPException

import db
import base_models
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is nomeroavto API"}

@app.get("/get-car-info/car-id")
async def get_car_info_by_car_id(car_id: int):
    car = db.Car.find_car_by_id(car_id)
    if car is None:
        raise HTTPException(404, "Car not found")
    return car.__dict__

@app.get("/get-car-info/plate-number")
async def get_car_info_by_plate_number(plate_number: str):
    if not re.match(r'^[0-9]{4}[ETIOPAHKXCBM]{2}[1-7]{1}$', plate_number):
        raise HTTPException(400,
                            "Plate number must match following regex:\n^[0-9]{4}[ETIOPAHKXCBM]{2}[1-7]{1}$")
    car = db.Car.find_car_by_plate_number(plate_number)
    if car is None:
        raise HTTPException(404, "Car not found")
    return car.__dict__
