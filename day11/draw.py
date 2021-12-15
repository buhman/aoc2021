import sys
import ctypes
import time
from sdl2 import *


def clear(stride, pixels):
    for i in range(500 * 500 * 4):
        pixels[i] = 0


def draw_rect(stride, pixels, y, x, color):
    for yi in range((y * 50), (y * 50) + 50):
        for xi in range((x * 50), (x * 50) + 50):
            for i in range(4):
                weight = (4 - ((i + 2) % 4)) / 4
                if color == 1:
                    pixels[(yi * stride + xi) * 4 + i] = 255
                else:
                    pixels[(yi * stride + xi) * 4 + i] = int(weight * color * 255)


import solution

board = list(solution.parse_input())
iteration = 0

def render(stride, pixels):
    global iteration
    iteration += 1
    print(iteration)
    global board
    clear(stride, pixels)
    flashed = solution.simulate_step(board)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if (y, x) in flashed:
                color = 1
            else:
                color = board[y][x] / 11

            draw_rect(stride, pixels, x, y, color)


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Hello World",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              500, 500, SDL_WINDOW_SHOWN)
    lp_surface = SDL_GetWindowSurface(window)
    surface = lp_surface.contents

    bpp = surface.format.contents.BytesPerPixel
    stride = surface.pitch // bpp

    running = True
    event = SDL_Event()
    last_time = time.time()
    while running:
        pixels = ctypes.cast(surface.pixels, ctypes.POINTER(Uint8))

        if time.time() - last_time > 0.01:
            render(stride, pixels)
            last_time = time.time()

        SDL_UpdateWindowSurface(window)

        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break

    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
