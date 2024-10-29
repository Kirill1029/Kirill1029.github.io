import json
import re
from typing import Annotated

from fastapi import FastAPI, HTTPException, UploadFile, Form

import db
import base_models
from db import Record

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



@app.post("/upload")
async def upload(car_id: Annotated[int, Form()], file: UploadFile | None = None):
    record = Record.add_new_record(car_id)
    if file is None:
        return record.__dict__
    extension = file.filename.split('.')[-1]
    file_bytes = await file.read()
    path = "cars/"+str(record.record_id)+"."+extension
    with open(path, 'wb') as image:
        image.write(file_bytes)
    record.update_photo(path)
    return record.__dict__
