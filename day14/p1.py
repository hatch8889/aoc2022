import pygame
empty = (0, 0, 0)
wall = (255, 255, 255)
sand = (255, 255, 0)


def drop_sand(screen, max_y):
    sands = 0
    x = 500
    snow = True
    while snow:
        tx = x
        snow = False
        for y in range(1, 199):
            if screen.get_at((tx, y)) != empty:
                break

            next_spot = screen.get_at((tx, y + 1))
            next_left = screen.get_at((tx - 1, y + 1))
            next_right = screen.get_at((tx + 1, y + 1))
            if next_spot == empty:
                continue

            if next_left == empty:
                tx = tx - 1
                continue

            if next_right == empty:
                tx = tx + 1
                continue

            if y > 190:
                # abyss
                break

            screen.set_at((tx, y), sand)
            snow = True  # send more sand
            sands += 1

    pygame.display.flip()
    print(sands)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(600, 200))
    screen.fill((0, 0, 0))
    max_y = 0

    with open('day14.txt') as data:
        for ss in data.read().splitlines():
            lines = ss.split(' -> ')
            for ii in range(1, len(lines)):
                st = tuple(map(int, lines[ii-1].split(',')))
                end = tuple(map(int, lines[ii].split(',')))
                pygame.draw.lines(screen, (255, 255, 255), False, [st, end], width=1)
                max_y = max([max_y, st[1], end[1]])

    pygame.display.flip()
    drop_sand(screen, max_y)

    while True:
        for et in pygame.event.get():
            if et.type == pygame.KEYDOWN:
                if (et.key == pygame.K_ESCAPE) or (et.type == pygame.QUIT):
                    exit()


if __name__ == '__main__':
    main()

# < 717
