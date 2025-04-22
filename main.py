from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> dict:
    serializer = CarSerializer(instance=car)
    return serializer.data


def deserialize_car_object(json_data: dict) -> Car:
    serializer = CarSerializer(data=json_data)
    serializer.is_valid(raise_exception=True)
    return Car(**serializer.validated_data)
