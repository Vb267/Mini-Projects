from turtle import Turtle
import random

COLORS = ["#e74c3c", "#f39c12", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6", "#1abc9c"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7
MAX_CARS_ON_SCREEN = 25


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if len(self.all_cars) < MAX_CARS_ON_SCREEN and random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-240, 260))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        # Remove off-screen cars
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
