import re
from typing import Annotated

from fastapi import FastAPI, HTTPException, UploadFile, Form
from fastapi.responses import FileResponse

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
    records = db.Record.find_car_records(car.id)
    return {'car': car.__dict__,
            'records': records}

@app.get("/get-car-info/plate-number")
async def get_car_info_by_plate_number(plate_number: str):
    if not re.match(r'^[0-9E]{4}[ETIOPAHKXCBM]{2}[1-7]$', plate_number):
        raise HTTPException(400,
                            "Plate number must match following regex:\n^[0-9E]{4}[ETIOPAHKXCBM]{2}[1-7]{1}$")
    car = db.Car.find_car_by_plate_number(plate_number)
    if car is None:
        raise HTTPException(404, "Car not found")
    records = db.Record.find_car_records(car.id)
    return {'car': car.__dict__,
            'records': records}



@app.post("/upload")
async def upload(car_id: Annotated[int, Form()], file: UploadFile | None = None,
                 timestamp: Annotated[int, Form()] = None,
                 description: Annotated[str, Form()] = None,
                 place: Annotated[str, Form()] = None, verified: Annotated[int, Form()] = 0):
    record = Record.add_new_record(car_id, None, timestamp,
                                   description, place, verified)
    if file is None:
        return record.__dict__
    extension = file.filename.split('.')[-1]
    file_bytes = await file.read()
    path = "cars/"+str(record.record_id)+"."+extension
    with open(path, 'wb') as image:
        image.write(file_bytes)
    record.update_photo(path)
    return record.__dict__


@app.post("/upload-by-plate")
async def upload_by_plate(plate_number: Annotated[str, Form()], file: UploadFile | None = None,
                 timestamp: Annotated[int, Form()] = None, description: Annotated[str, Form()] = None,
                 place: Annotated[str, Form()] = None, verified: Annotated[int, Form()] = 0):
    if not re.match(r'^[0-9E]{4}[ETIOPAHKXCBM]{2}[1-7]$', plate_number):
        raise HTTPException(400,
                            "Plate number must match following regex:\n^[0-9E]{4}[ETIOPAHKXCBM]{2}[1-7]{1}$")
    record = Record.add_new_record_by_plate(plate_number, None, timestamp,
                                            description, place, verified)
    if file is None:
        return record.__dict__
    extension = file.filename.split('.')[-1]
    file_bytes = await file.read()
    path = "cars/"+str(record.record_id)+"."+extension
    with open(path, 'wb') as image:
        image.write(file_bytes)
    record.update_photo(path)
    return record.__dict__


@app.get("/get-photo")
async def get_photo(photo_id: str):
    return FileResponse(photo_id)
