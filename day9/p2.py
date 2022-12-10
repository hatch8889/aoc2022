import math
import pygame
import time

visited = set([(0, 0)])
screen: pygame.Surface

rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]


def rc(c: tuple[int, int]) -> pygame.rect:
    h = 3
    return pygame.Rect(h*c[0] + 200, h*c[1] + 900, h, h)


def draw_scene():
    global screen
    screen.fill((0, 0, 0))

    for x in visited:
        pygame.draw.rect(screen, (100, 100, 100), rc(x))

    # origin
    pygame.draw.rect(screen, (0, 255, 0), rc((0, 0)))
    # tail
    for ii in range(0, 10):
        x = rope[ii]
        pygame.draw.rect(screen, (255, int(24*ii), 0), rc(x))

    pygame.display.flip()
    time.sleep(0.01)


def get_dist(h, t) -> float:
    return math.sqrt((h[0] - t[0])**2 + (h[1] - t[1])**2)


def move_tail(h, t):
    # transpose head, so tail is at 0,0
    new_head = (h[0] - t[0], h[1] - t[1])
    if new_head[0] >= 1 and new_head[1] >= 1:
        o = move(t, 'D')
        o = move(o, 'R')
    elif new_head[0] >= 1 and new_head[1] <= -1:
        o = move(t, 'U')
        o = move(o, 'R')
    elif new_head[0] <= -1 and new_head[1] <= -1:
        o = move(t, 'U')
        o = move(o, 'L')
    elif new_head[0] <= -1 and new_head[1] >= 1:
        o = move(t, 'D')
        o = move(o, 'L')
    elif new_head[1] < -1:
        o = move(t, 'U')
    elif new_head[1] > 1:
        o = move(t, 'D')
    elif new_head[0] > 1:
        o = move(t, 'R')
    elif new_head[0] < -1:
        o = move(t, 'L')
    else:
        raise 'oops'
    return o


def move(pos: tuple[int, int], direction: str) -> tuple[int, int]:
    if direction == 'D':
        return pos[0], pos[1] + 1
    if direction == 'U':
        return pos[0], pos[1] - 1
    if direction == 'R':
        return pos[0] + 1, pos[1]
    if direction == 'L':
        return pos[0] - 1, pos[1]

    return pos


def step(direction: str):
    rope[0] = move(rope[0], direction)

    for ii in range(1, 10):
        dist = get_dist(rope[ii-1], rope[ii])
        if dist > 1.5:
            rope[ii] = move_tail(rope[ii-1], rope[ii])

    visited.add(rope[9])

    draw_scene()


def calc(direction: str, steps: int):
    for _ in range(0, steps):
        step(direction)


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(size=(1024, 1024))
    with open('day9.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            parts = line.split(' ')
            calc(parts[0], int(parts[1]))
        print(len(visited))

        while True:
            for et in pygame.event.get():
                if et.type == pygame.KEYDOWN:
                    if (et.key == pygame.K_ESCAPE) or (et.type == pygame.QUIT):
                        exit()


if __name__ == '__main__':
    main()
