#!/usr/bin/env python
import pygame as pg

REZ_X = 64
REZ_Y = 64
RENDER_REZ_X = 512
RENDER_REZ_Y = 512

GREEN = pg.Color(0, 255,0)
BLACK = pg.Color(0,0,0)
RED = pg.Color(255,0,0)
BLUE = pg.Color(0,0,255)

def add_some_pixels(surface):
    ar = pg.PixelArray(surface)
    # sand
    for i in range(1, 15):
        ar[32,i] = BLACK
    # water
    for i in range(1, 15):
        ar[44,i] = BLUE
        ar[45,i] = BLUE
    # add some solid RED
    for i in range(64):
        ar[i,63] = RED
    ar[41,60] = RED
    ar[48,60] = RED
    ar[42,61] = RED
    ar[47,61] = RED
    ar[43,62] = RED
    ar[46,62] = RED
    del ar
    return surface

def sand(surface, x,y):
    ar = pg.PixelArray(surface)
    if ar[x,y] == surface.map_rgb(BLACK):
        if ar[x,y+1] == surface.map_rgb(GREEN):
            ar[x,y+1] = BLACK
            ar[x,y] = GREEN
        elif ar[x -1, y+1] == surface.map_rgb(GREEN):
            ar[x -1, y+1] = BLACK
            ar[x,y] = GREEN
        elif ar[x+1, y+1] == surface.map_rgb(GREEN):
            ar[x+1, y+1] = BLACK
            ar[x,y] = GREEN
    del ar
    return surface

def water(surface, x,y):
    ar = pg.PixelArray(surface)
    if ar[x,y] == surface.map_rgb(BLUE):
        if ar[x,y+1] == surface.map_rgb(GREEN):
            ar[x,y+1] = BLUE
            ar[x,y] = GREEN
        elif ar[x -1, y+1] == surface.map_rgb(GREEN):
            ar[x -1, y+1] = BLUE
            ar[x,y] = GREEN
        elif ar[x+1, y+1] == surface.map_rgb(GREEN):
            ar[x+1, y+1] = BLUE
            ar[x,y] = GREEN
        elif ar[x-1, y] == surface.map_rgb(GREEN):
            ar[x-1, y] = BLUE
            ar[x,y] = GREEN
        elif ar[x+1, y] == surface.map_rgb(GREEN):
            ar[x+1, y] = BLUE
            ar[x,y] = GREEN
    del ar
    return surface

def physics(surface):
    for x in range(REZ_X):
        for y in range(REZ_Y-1, 0, -1):
            surface = sand(surface, x, y)
            surface = water(surface, x, y)
    return surface

def reset_state(surface):
    surface.fill(GREEN)
    add_some_pixels(surface)

def main():
    pg.init()
    pg.display.set_mode((RENDER_REZ_X, RENDER_REZ_Y))
    surface = pg.Surface((REZ_X, REZ_Y))
    reset_state(surface)
    pg.display.flip()
    clock = pg.time.Clock()

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise SystemExit
            if event.type in [pg.KEYDOWN]:
                if event.key == pg.K_SPACE:
                    reset_state(surface)
            if event.type in [pg.MOUSEBUTTONDOWN, pg.KEYDOWN]:
                break
        surface = physics(surface)
        screen = pg.display.get_surface()
        # do up scaling
        pg.transform.scale(surface, (RENDER_REZ_X, RENDER_REZ_Y), screen)
        pg.display.update()
        clock.tick(60) # fps
    pg.quit()


if __name__ == "__main__":
    main()
