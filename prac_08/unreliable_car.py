from random import randint
from prac_08.car import Car

class UnreliableCar(Car):

    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.reliability, self.price_per_km)

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven