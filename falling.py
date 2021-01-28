#!/usr/bin/env python
import pygame as pg

REZ_X = 64
REZ_Y = 64
RENDER_REZ_X = 512
RENDER_REZ_Y = 512

green = pg.Color(0, 255,0)
black = pg.Color(0,0,0)
red = pg.Color(255,0,0)

def add_some_pixels(surface):
    ar = pg.PixelArray(surface)
    ar[32,2] = black
    ar[32,3] = black
    ar[32,4] = black
    ar[32,5] = black
    ar[32,6] = black
    ar[32,7] = black
    ar[32,8] = black
    ar[32,9] = black
    ar[32,10] = black
    ar[32,11] = black
    ar[32,12] = black
    ar[32,13] = black
    ar[32,14] = black
    ar[52,51] = black
    ar[52,52] = black
    ar[52,53] = black
    ar[52,54] = black
    # add a red line for sand to land on
    for i in range(64):
        ar[i,54] = red
    del ar
    return surface

def sand(surface, x,y):
    ar = pg.PixelArray(surface)
    if ar[x,y] == surface.map_rgb(black):
        if ar[x,y+1] == surface.map_rgb(green):
            ar[x,y+1] = black
            ar[x,y] = green
        elif ar[x -1, y+1] == surface.map_rgb(green):
            ar[x -1, y+1] = black
            ar[x,y] = green
        elif ar[x+1, y+1] == surface.map_rgb(green):
            ar[x+1, y+1] = black
            ar[x,y] = green
    del ar
    return surface

def physics(surface):
    for x in range(REZ_X):
        for y in range(REZ_Y-1, 0, -1):
            surface = sand(surface, x, y)
    return surface

def reset_state(surface):
    surface.fill(green)
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
