class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy: bool = False):
        """

        :param color: цвет
        :param count_passenger_seats: количество пассажирских мест
        :param is_baby_seat: наличие десткого кресла
        :param is_busy: определяется внутри конструктора со значением False, не принимается на вход
        """
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat

    def __str__(self):
        return f"Car color: {self.color}" \
               f", passanger seats: {self.count_passenger_seats}, baby seat exists: {'Yes' if self.is_baby_seat else 'No'}"


new_car = Car("red", 4, 0)
print(new_car)
