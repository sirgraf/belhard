from task_8_1 import Car


class Taxi:

    def __init__(self, cars: list[Car]):
        self.cars = cars

    def __str__(self):
        result = ""
        for x in self.cars:
            result += str(x) + "\n"
        return result

    def find_car(self, count_passengers: int, is_baby: bool) -> Car:
        res = list(filter(lambda
                              x: x.count_passenger_seats >= count_passengers + is_baby and x.is_baby_seat == is_baby and not x.is_busy,
                          self.cars))
        try:
            res[0].is_busy = True
            return res[0]
        except IndexError:
            return None


obj_taxi = Taxi([Car("red", 4, True), Car("black", 3, False)])
print(obj_taxi.find_car(3, True))
print(obj_taxi.find_car(3, True))
print(obj_taxi)
