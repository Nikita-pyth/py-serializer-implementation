from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64, default="")
    model = serializers.CharField(max_length=64, default="")
    horse_powers = serializers.IntegerField(min_value=1,
                                            max_value=1914,
                                            default=None)
    is_broken = serializers.BooleanField(default=False)
    problem_description = serializers.CharField(required=False)

    def serialize_car_object(self, car: Car) -> dict:
        serializer = CarSerializer(instance=car)
        return serializer.data

    def deserialize_car_object(self, json_data: dict) -> Car:
        serializer = CarSerializer(data=json_data)
        serializer.is_valid(raise_exception=True)
        return Car(**serializer.validated_data)
