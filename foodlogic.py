def bacteria_food_connection(key, bacteria, food, FOOD_OBJECT_LIMIT, Food, reset, FOODS):
    if len(bacteria) > len(food) and len(food) <= FOOD_OBJECT_LIMIT:
        addition = len(bacteria) - len(food)
        for i in range(addition):
            food.append(Food())
    if key == 1 and reset == 1:
        for i in food:
            i.hideturtle()
        food.clear()
        for i in range(FOODS):
            food.append(Food())
