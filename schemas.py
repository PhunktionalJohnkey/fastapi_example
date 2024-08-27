from sqlmodel import SQLModel, Field
import json

class TripInput(SQLModel):
    start: int
    end: int
    description: str


class TripOutput(TripInput):
    id: int


class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

    class Config:
        schema_extra = {
            "example": {
                "size": "m",
                "doors": 5,
                "transmission": "manual",
                "fuel": "hybrid"
            }
        }


class Car(CarInput, table=True):
    id: int | None = Field(primary_key=True, default=None)

class CarOutput(CarInput):
    id: int
    trips: list[TripOutput] = []


def load_db() -> list[CarOutput]:
    """Load a list of Car objects from a JSON file"""
    with open("cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]


def save_db(cars: list[CarOutput]):
    with open("cars.json", 'w') as f:
        json.dump([car.dict() for car in cars], f, indent=4)

