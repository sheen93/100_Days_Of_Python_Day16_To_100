from vehicle import Vehicle, Sedan, Bus, BigTruck, SUV, MotorCycle
import random

CAR_SPEED = 10
LANE_POS = [-200,-130,-60,60,130,200]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.moving_speed = CAR_SPEED

    def create_cars(self):
        if random.randint(1,6) == 1:
            random_y_cor = random.choice(LANE_POS)
            car_type = random.choice([Sedan, Bus, BigTruck, SUV, MotorCycle])

            safe_to_spawn = True
            for car in self.all_cars:
                if car.ycor() == random_y_cor:
                    if abs(car.xcor()) > 350:
                        safe_to_spawn = False
                        break

            if safe_to_spawn:
                if random_y_cor < 0:
                    new_car = car_type(lane_pos=random_y_cor, direction=0)
                else:
                    new_car = car_type(lane_pos=random_y_cor, direction=180)
                self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars[:]:
            car.forward(self.moving_speed)

            if car.xcor() > 620 or car.xcor() < -620:
                car.hideturtle()
                self.all_cars.remove(car)

    def speed_up(self):
        self.moving_speed += 5