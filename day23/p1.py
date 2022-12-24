from collections import defaultdict
import pygame

try_moves = [[(-1, -1), (0, -1), (1, -1)],
             [(1, 1), (0, 1), (-1, 1)],
             [(-1, 1), (-1, 0), (-1, -1)],
             [(1, -1), (1, 0), (1, 1)]]
adjacent = [(-1, -1), (0, -1), (1, -1), (1, 1), (0, 1), (-1, 1), (-1, 0), (1, 0)]


class Game:
    board: set
    screen: pygame.Surface
    size = 10

    def __init__(self):
        self.board = set()
        with open('data.txt') as data:
            lines = data.read().splitlines()
            for y in range(len(lines)):
                line = lines[y]
                for x in range(len(line)):
                    block = line[x]
                    if block == '#':
                        self.board.add((x, y))

        pygame.init()
        self.screen = pygame.display.set_mode(size=(self.size * 100, self.size * 100))
        self.draw()
        self.wait_key()

    def step(self, round: int):
        proposals = defaultdict(lambda: [])

        for elf in self.board:
            if not any((elf[0] + looking[0], elf[1] + looking[1]) in self.board for looking in adjacent):
                continue

            for ii in range(4):
                direction = (round + ii) % 4
                taken = False
                for move in try_moves[direction]:
                    if (elf[0] + move[0], elf[1] + move[1]) in self.board:
                        taken = True
                        break
                if not taken:
                    move = try_moves[direction][1]
                    proposals[(elf[0] + move[0], elf[1] + move[1])].append(elf)
                    break

        for proposal in proposals:
            if len(proposals[proposal]) == 1:
                self.board.remove(proposals[proposal][0])
                self.board.add(proposal)

        return len(proposals) == 0

    def rc(self, c: tuple[int, int]) -> pygame.rect:
        mid = self.size * 10

        return pygame.Rect((self.size * c[0]) + mid, (self.size * c[1]) + mid, self.size, self.size)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for p in self.board:
             pygame.draw.rect(self.screen, (100, 100, 100), self.rc(p))
        pygame.display.flip()

    def area(self):
        xs = list(map(lambda p: p[0], self.board))
        ys = list(map(lambda p: p[1], self.board))

        return sum((x, y) not in self.board for y in range(min(ys), max(ys) + 1) for x in range(min(xs), max(xs) + 1))

    def wait_key(self):
        while True:
            for et in pygame.event.get():
                if et.type == pygame.QUIT:
                    exit(0)

                if et.type == pygame.KEYDOWN:
                    return


def main():
    game = Game()

    for ii in range(10):
        zz = game.step(ii)
        if zz:
            break
    print('part1: ', game.area())


if __name__ == '__main__':
    main()
