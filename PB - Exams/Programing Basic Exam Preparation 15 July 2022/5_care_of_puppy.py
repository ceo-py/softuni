kg_dog_food = int(input())

kg_dog_food *= 1000

eaten_food_per_day = input()

while eaten_food_per_day != "Adopted":
    eaten_food = int(eaten_food_per_day)
    kg_dog_food -= eaten_food
    eaten_food_per_day = input()


if kg_dog_food  >= 0:
    print(f"Food is enough! Leftovers: {kg_dog_food} grams." )

else:
    print(f"Food is not enough. You need {abs(kg_dog_food)} grams more.")