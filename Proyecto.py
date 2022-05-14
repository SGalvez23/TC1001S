# Se importan librerias
from re import S
from turtle import *
from freegames import floor, vector

# Se definen variables generales del juego / Sebastian Galvez
path = Turtle(visible=False)
pacman = vector(-180, 190)
key1 = vector(-180, -180)
key2 = vector(-140, -100)
key3 = vector(40, 100)
aim = vector(0, 0)
state ={"key1": False, "key2":False, "key3":False, "win": False}
door = vector(160,-180)

# Matriz que conforma la estructura del Mapa / Sebastian Galvez
tiles = [
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Cuadros utilizados en el mapa / Sebastian Galvez
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

# Esta funcion declara donde esta apuntando el jugador / Cesar Galvez
def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Esta funcion declara si el jugador esta apuntado a una pared no lo deja avanzar / Alam Lopez
def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

# Esta funcion funciona para dibujar el mapa conforme a los valores introducidos en la variable de tiles / Alam Lopez
def world():
    "Draw world using path."
    bgcolor('black')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20

            if tile == 1:
                path.color('white')
                square(x, y)
            
            if tile == 2:
                path.color('green')
                square(x, y)

            if tile == 3:
                if state['win'] == False:
                    path.color('red')
                    square(x,y)
                else:
                    path.color('blue')
                    square(x,y)

# Funcion para que el jugador se pueda mover / Rodolfo Bojorquez
def move():
    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)
    
    if tiles[index] == 1:         
        path.color('green')
        tiles[index] = 2
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
    
    # Condicion para que el jugador pueda ganar
    if tiles[index] == 3 and state['win'] == True:         
        path.clear()
        up()
        goto(0,0)
        
        color("white")
        write("GANASTE!!", font=("Comic Sans",50, "normal",) ,align="center")
        input("Enter..")
        quit()

    if pacman.x == key1.x and pacman.y ==key1.y:
        state['key1'] = True

    if pacman.x == key2.x and pacman.y ==key2.y:
        state['key2'] = True

    if pacman.x == key3.x and pacman.y ==key3.y:
        state['key3'] = True

    if state['win'] == False and state['key1'] == True and state['key2'] == True and state['key3'] == True:
        state['win'] = True
        world()
    

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    if state['key1'] == False:
        up()
        goto(key1.x + 10, key1.y + 10)
        dot(10, 'blue')

    if state['key2'] == False:
        up()
        goto(key2.x + 10, key2.y + 10)
        dot(10, 'blue')

    if state['key3'] == False:
        up()
        goto(key3.x + 10, key3.y + 10)
        dot(10, 'blue')




    update()
    ontimer(move, 70)

# Funcion para cambiar la direccion del jugador si hay un camino disponible / Cesar Galvez
def change(x, y):
    """Change aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y
                
setup(480, 500, 370, 0)
hideturtle()
tracer(False)
world()
listen()
# Se definen las teclas con las cuales se podra mover el jugador y la velocidad de dicho movimiento / Cesar Galvez
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move()
done()