from turtle import Turtle
from random import randint, choice
MAP_SIZE = 250  # ONLY SQUARE MAPS! one side length
NOURISHMENT = 50  # how many hunger points bacteria have
AGE = 0  # starting bacteria age


class Bacteria(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.age = AGE
        self.nourishment = NOURISHMENT
        self.goto(randint(-MAP_SIZE + 20, MAP_SIZE - 20), randint(-MAP_SIZE + 20, MAP_SIZE - 20))

    def move(self):
        current_position = self.position()
        new_direction = choice([0, 90, 180, 270])
        self.seth(new_direction)
        self.forward(40)
        if list(self.position())[0] > MAP_SIZE - 20 or list(self.position())[0] < -MAP_SIZE + 20 or \
                list(self.position())[1] > MAP_SIZE - 20 or list(self.position())[1] < -MAP_SIZE + 20:
            self.goto(current_position)
            self.move()
