from turtle import Screen
from time import sleep
from food import Food
from bacteria import Bacteria
from foodlogic import bacteria_food_connection

HUNGER = 1  # how many points of hungriness bacteria lose
AGEING = 1  # how old bacteria become after on iteration
FOODS = 5  # amount of food objects the simulation starts with
BACTERIA = 1  # amount of bacteria objects the simulation starts with
HUNGER_POINTS = 25  # how many hunger points bacteria get after eating a food object
BREEDING_AGE = 10  # age when bacteria can breed
BREEDING_HUNGER = 25  # how many hunger points bacteria lose after breeding
BREEDING_HUNGER_NEEDED = 50  # how many points(at least) bacteria should have to breed
DEATH_AGE = 50  # age when bacteria die
HUNGER_DEATH = 0   # the number of hunger points that leads to bacteria death
FOOD_OBJECT_LIMIT = 10  # the number of food object that can be on the map. There are as many
# food objects as bacteria objects. But if all bacteria die the amount of food objects stays the same
FOOD_LOGIC = 1  # if this var is   0    than FOOD_OBJECT_LIMIT makes sense, elif this var is  1  than if all bacteria
# die the amount of food objects resets to the starting amount

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Evolve")
screen.tracer(0)

food = []
for i in range(FOODS):
    new_food = Food()
    food.append(new_food)

bacteria = []
for i in range(BACTERIA):
    new_bact = Bacteria()
    bacteria.append(new_bact)

reset = 0

while True:
    sleep(0.1)
    for bact in bacteria:
        bact.move()
        for snack in food:
            if bact.distance(snack.position()) < 20:
                snack.change_place()
                bact.nourishment += HUNGER_POINTS

        bact.age += AGEING
        bact.nourishment -= HUNGER

        if bact.age >= BREEDING_AGE and bact.nourishment >= BREEDING_HUNGER_NEEDED:
            bacteria.append(Bacteria())
            bact.nourishment -= BREEDING_HUNGER

        if bact.age == DEATH_AGE or bact.nourishment == HUNGER_DEATH:
            bact.color("brown")
            bacteria.remove(bact)

        if len(bacteria) == 0:
            for i in range(BACTERIA):
                new_bact = Bacteria()
                bacteria.append(new_bact)
                reset = 1

        bacteria_food_connection(FOOD_LOGIC, bacteria, food, FOOD_OBJECT_LIMIT, Food, reset, FOODS)
        reset = 0

    screen.update()

