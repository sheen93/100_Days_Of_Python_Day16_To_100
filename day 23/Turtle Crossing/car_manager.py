from vehicle import Vehicle

LANE_POS = []

class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_cars()

    def create_cars(self):
        new_car = Vehicle()
        self.car_list.append(new_car)
        new_car.goto()

    def move_cars(self):
        pass