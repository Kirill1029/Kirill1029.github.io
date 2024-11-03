import sqlite3
from sqlite3 import Connection
from typing import Callable

connection = sqlite3.connect('users.sqlite')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
user_id INTEGER PRIMARY_KEY,
accepted INTEGER
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS "Cars" (
	"car_id"	INTEGER,
	"plate_number"	TEXT NOT NULL UNIQUE,
	"model" TEXT,
	"volume"	INTEGER,
	"color"	TEXT,
	"power"	INTEGER,
	"vehicle_type"	TEXT,
	PRIMARY KEY("car_id" AUTOINCREMENT)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS "Records" (
	"record_id"	INTEGER NOT NULL,
	"car_id"	INTEGER NOT NULL,
	"photo_id"	TEXT,
	"timestamp"	INTEGER,
	"description"	TEXT,
	"place"	TEXT,
	"verified"	INTEGER,
	PRIMARY KEY("record_id" AUTOINCREMENT)
)''')

connection.close()

def connect(func: Callable):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('users.sqlite')
        res = func(*args, **kwargs, connection=connection)
        connection.commit()
        connection.close()
        return res
    return wrapper

# @connect
# def add_new_user(user_id: int, accepted: int = 0, connection: Connection = None):
#     cursor = connection.cursor()
#     cursor.execute(f"INSERT INTO Users VALUES ({user_id}, {accepted})")
#

class User:
    def __init__(self, user_id: int, accepted: int = 0):
        self.user_id = user_id
        self.accepted = accepted

    @staticmethod
    @connect
    def exists(user_id: int, connection: Connection = None):
        cursor = connection.cursor()
        return cursor.execute(f"SELECT COUNT(*) FROM Users WHERE user_id={user_id}").fetchone()[0] == 1

    @staticmethod
    @connect
    def add_new_user(user_id: int, accepted: int = 0, connection: Connection = None):
        if not User.exists(user_id):
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO Users VALUES ({user_id}, {accepted})")
        return User(user_id, accepted)

    @connect
    def update_terms_status(self, accepted_status: int, connection: Connection = None):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Users SET accepted={accepted_status} WHERE user_id={self.user_id}")
        self.accepted = accepted_status

    @staticmethod
    @connect
    def find_user(user_id: int, connection: Connection = None):
        cursor = connection.cursor()
        res = cursor.execute(f"SELECT * FROM Users WHERE user_id={user_id}").fetchone()
        if res is None:
            return None
        return User(res[0], res[1])


class Car:
    def __init__(self, car_id: int, plate_number: str, model: str = None,
                 volume: int = None, color: str = None,
                 power: int = None, vehicle_type: str = None):
        self.id = car_id
        self.plate_number = plate_number
        self.model = model
        self.volume = volume
        self.color = color
        self.power = power
        self.vehicle_type = vehicle_type

    @staticmethod
    @connect
    def exists(car_id: int, connection: Connection = None):
        cursor = connection.cursor()
        return cursor.execute(f"SELECT COUNT(*) "
                              f"FROM Cars "
                              f"WHERE car_id={car_id}").fetchone()[0] == 1

    @staticmethod
    @connect
    def add_new_car(plate_number: str, model: str = None,
                    volume: int = None, color: str = None,
                    power: int = None, vehicle_type: str = None,
                    connection: Connection = None):
        cursor = connection.cursor()
        car_id = cursor.execute(f'SELECT COUNT(car_id) FROM Cars').fetchone()[0]
        cursor.execute(f"INSERT INTO Cars VALUES"
                       f"("
                       f"'{car_id+1}',"
                       f"'{plate_number}', "
                       f"'{model if model is None else 'NULL'}', "
                       f"'{volume if volume is None else 'NULL'}',"
                       f"'{color if color is None else 'NULL'}',"
                       f"'{power if power is None else 'NULL'}', "
                       f"'{vehicle_type if vehicle_type is None else 'NULL'}'"
                       f")")
        return Car(car_id+1, plate_number, model,
                   volume, color, power, vehicle_type)

    @connect
    def update_model(self, model: str, connection: Connection = None):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Cars SET model='{model}' WHERE car_id='{self.id}'")

    @connect
    def update_volume(self, volume: int, connection: Connection = None):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Cars SET volume='{volume}' WHERE car_id='{self.id}'")

    @connect
    def update_color(self, color: str, connection: Connection = None):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Cars SET color='{color}' WHERE car_id='{self.id}'")

    @connect
    def update_power(self, power: int, connection: Connection = None):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Cars SET power='{power}' WHERE car_id='{self.id}'")

    @connect
    def update_vehicle_type(self, vehicle_type: int, connection: Connection = None):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Cars SET vehicle_type='{vehicle_type}' WHERE car_id='{self.id}'")

    @staticmethod
    @connect
    def find_car_by_id(car_id: int, connection: Connection = None):
        cursor = connection.cursor()
        res = cursor.execute(f"SELECT * FROM Cars WHERE car_id={car_id}").fetchone()
        if res is None:
            return None
        return Car(*res)

    @staticmethod
    @connect
    def find_car_by_plate_number(plate_number: str, connection: Connection = None):
        cursor = connection.cursor()
        res = cursor.execute(f"SELECT * FROM Cars WHERE plate_number='{plate_number}'").fetchone()
        if res is None:
            return None
        return Car(*res)


class Record:
    def __init__(self, record_id: int, car_id: int, photo_id: str = None,
                 timestamp: int = None, description: str = None,
                 place: str = None, verified: int = 0):
        self.record_id = record_id
        self.car_id = car_id
        self.photo_id = photo_id
        self.timestamp = timestamp
        self.description = description
        self.place = place
        self.verified = verified

    @staticmethod
    @connect
    def find_record_by_id(record_id: int, connection: Connection):
        cursor = connection.cursor()
        res = cursor.execute(f"SELECT * FROM Records WHERE record_id={record_id}").fetchone()
        if res is None:
            return None
        return Record(*res)

    @staticmethod
    @connect
    def find_car_records(car_id: int, connection: Connection):
        cursor = connection.cursor()
        res = cursor.execute(f"SELECT * FROM Records WHERE car_id={car_id} ORDER BY timestamp DESC").fetchall()
        ans = []
        for row in res:
            ans.append(Record(*row))
        return ans

    @staticmethod
    @connect
    def add_new_record_by_plate(plate_number: str, photo_id: str = None, timestamp: int = None,
                       description: str = None, place: str = None,
                       verified: int = 0, connection: Connection = None):
        cursor = connection.cursor()
        record_id = cursor.execute(f'SELECT COUNT(record_id) FROM Records').fetchone()[0]
        car = Car.find_car_by_plate_number(plate_number)
        if car is None:
            car = Car.add_new_car(plate_number)
        cursor.execute(f'INSERT INTO Records VALUES({record_id+1}, '
                       f'"{car.id}", '
                       f'"{"NULL" if photo_id is None else photo_id}",'
                       f'"{timestamp}",'
                       f'"{"NULL" if description is None else description}",'
                       f'"{place}",'
                       f'"{verified}"'
                       f')')
        return Record(record_id+1, car.id, photo_id, timestamp, description, place, verified)

    @staticmethod
    @connect
    def add_new_record(car_id: int, photo_id: str = None, timestamp: int = None,
                       description: str = None, place: str = None,
                       verified: int = 0, connection: Connection = None):
        cursor = connection.cursor()
        record_id = cursor.execute(f'SELECT COUNT(record_id) FROM Records').fetchone()[0]
        cursor.execute(f'INSERT INTO Records VALUES({record_id + 1}, '
                       f'"{car_id}", '
                       f'"{"NULL" if photo_id is None else photo_id}",'
                       f'"{timestamp}",'
                       f'"{"NULL" if description is None else description}",'
                       f'"{place}",'
                       f'"{verified}"'
                       f')')
        return Record(record_id + 1, car_id, photo_id, timestamp, description, place, verified)

    @connect
    def update_photo(self, new_photo_id: str, connection: Connection):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Records SET photo_id='{new_photo_id}' WHERE record_id={self.record_id}")
        self.photo_id = new_photo_id
