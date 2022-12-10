import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(1024, 512))
    screen.fill((0, 0, 0))

    with open('day10.txt') as data:
        lines = data.read().splitlines()
        cycle = 0
        exec_step = -1
        instr = ''
        running = True
        x = 1
        cnt = 0
        strengths = []

        while running:
            cycle += 1
            exec_step -= 1

            if exec_step <= 0:
                if instr.startswith('addx'):
                    x += int(instr.split(' ')[1])

                if cnt < len(lines):
                    instr = lines[cnt]
                    cnt += 1
                else:
                    running = False

                if instr.startswith('addx'):
                    exec_step = 2
                elif instr.startswith('noop'):
                    exec_step = 1

            if (cycle - 20) % 40 == 0:
                strengths.append(cycle * x)

            line = (cycle - 1) // 40
            pos = (cycle - 1) % 40
            if x == pos - 1 or x == pos or x == pos + 1:
                h = 20
                pygame.draw.rect(screen, (255, 255, 255), (h*pos, h*line + h, h, h))
                pygame.display.flip()

        print('Part 1: ')
        print(sum(strengths))

        while True:
            for et in pygame.event.get():
                if et.type == pygame.KEYDOWN:
                    if (et.key == pygame.K_ESCAPE) or (et.type == pygame.QUIT):
                        exit()


if __name__ == '__main__':
    main()
