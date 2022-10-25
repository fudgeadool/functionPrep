from add import add_fruit
from divide import div_fruit
from multi import multi_fruit


apples = int(input("How many apples?"))
oranges = int(input("how many oranges?"))

#function call for adding apples and oranges
fruit = add_fruit(apples,oranges)
print(fruit)


#function for dividing apples and oranges
divide = div_fruit(apples,oranges)
print(divide)
#function for multiplying apples and oranges
multiply = multi_fruit(apples,oranges)
print(multiply)