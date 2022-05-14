from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Cambio de Color de Serpiente y Comida / Alam Lopez
list = [0, 1, 2, 3, 4]
i = random.choice(list)

if i == 0: 
    color_snake = 'blue'
    color_food = 'purple'
if i == 1: 
    color_snake = 'orange'
    color_food = 'black'
if i == 2: 
    color_snake = 'purple'
    color_food = 'yellow'
if i == 3: 
    color_snake = 'pink'
    color_food = 'blue'
if i == 4: 
    color_snake = 'black'
    color_food = 'green'

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
       
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_snake)

    square(food.x, food.y, 9, color_food)

    update()
    ontimer(move, 100)

# Funcion para mover la comida cada cierto tiempo / Sebastian Galvez
def rand_food():
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
    ontimer(rand_food, 6000)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
rand_food()
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move()
done()