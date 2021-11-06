from os import system
from keyboard import add_hotkey
from time import sleep as pause
from random import randint

# controls
x_mod = 0
y_mod = 0


def up():
    global x_mod, y_mod
    if not y_mod == 1:
        y_mod = -1
        x_mod = 0


def down():
    global x_mod, y_mod
    if not y_mod == -1:
        y_mod = 1
        x_mod = 0


def left():
    global x_mod, y_mod
    if not x_mod == 1:
        y_mod = 0
        x_mod = -1


def right():
    global x_mod, y_mod
    if not x_mod == -1:
        y_mod = 0
        x_mod = 1


add_hotkey('Up', up)
add_hotkey('Down', down)
add_hotkey('Left', left)
add_hotkey('Right', right)
# controls _

# field
field_size = 10
grass = '*'
game_field = [[grass for _ in range(field_size)] for _ in range(field_size)]
x = 1
y = field_size - 1

# snake
snake = 1
head = 'X'
tail = 'O'
tail_D = {n: [0, 0] for n in range(1, field_size ** 2)}
m = 1


# apples
apple = 'A'


def apple_spawn():
    fax = randint(0, field_size - 1)
    fay = randint(0, field_size - 1)
    global game_field
    if game_field[fay][fax] != grass:
        fay, fax = apple_spawn()
    return fay, fax


ay, ax = apple_spawn()

# game cycle
system("cls")
right()
tail_D[1][0] = y
tail_D[1][1] = x
while True:
    if m < len(tail_D):
        m += 1
    for j in range(m, 1, -1):
        tail_D[j][0] = tail_D[j - 1][0]
        tail_D[j][1] = tail_D[j - 1][1]
    tail_D[1][0] = y
    tail_D[1][1] = x
    game_field = [[grass for _ in range(field_size)] for _ in range(field_size)]
    game_field[ay][ax] = apple
    y += y_mod
    x += x_mod
    if x < 0 or x >= field_size or y < 0 or y >= field_size:
        break
    for g in range(snake - 1):
        game_field[tail_D[g+1][0]][tail_D[g+1][1]] = tail
    if game_field[y][x] == apple:
        snake += 1
        ay, ax = apple_spawn()
        game_field[ay][ax] = apple
    if game_field[y][x] != grass and game_field[y][x] != apple:
        break
    game_field[y][x] = head
    for ln in game_field:
        print(*ln)
    print('', '', 'Score: '+str(snake - 1), sep='\n')
    pause(0.5)
    system('cls')

print('Game Over!\nYour score: '+str(snake - 1))
input('Press enter to exit.')
