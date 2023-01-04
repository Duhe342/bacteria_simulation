from turtle import Turtle
from random import randint
MAP_SIZE = 250  # ONLY SQUARE MAPS! one side length


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.goto(randint(-MAP_SIZE + 20, MAP_SIZE - 20), randint(-MAP_SIZE + 20, MAP_SIZE - 20))

    def change_place(self):
        self.goto(randint(-MAP_SIZE + 20, MAP_SIZE - 20), randint(-MAP_SIZE + 20, MAP_SIZE - 20))
