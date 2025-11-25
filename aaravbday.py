
import os
import time
x = 100
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

import pgzrun

WIDTH = 1100
HEIGHT = 650
year_x = -80
year_y = 280
cake_x = -1000
cake_y = 300
aarav_x = 50
aarav_y = -3000
def draw():
    global year_x, year_y, cake_x, cake_y, aarav_x, aarav_y
    screen.clear()
    screen.blit("fireworksbigger",(35,40))
    screen.blit("small13", (year_x, year_y)) 
    screen.blit("cake", (cake_x, cake_y))
    screen.blit("aarav", (aarav_x, aarav_y))
 #   time.sleep(1)
    year_x = year_x + 15
    cake_x += 15
    if aarav_y < (HEIGHT // 4) - 500:
        aarav_y += 8



def update():
    pass

pgzrun.go()