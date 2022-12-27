import heapq
from math import lcm
import pygame
import time


class Game:
    edge: set
    tornado_left: set
    screen: pygame.Surface
    size = 10
    start = (1, 0)
    end: tuple
    path: list
    max_x = 0
    max_y = 0
    possible_moves = 0

    def __init__(self):
        self.edge = set()
        self.tornado_left = set()
        self.tornado_up = set()
        self.tornado_right = set()
        self.tornado_down = set()
        self.path = []

        with open('test.txt') as data:
            lines = data.read().splitlines()
            for y in range(len(lines)):
                if y > self.max_y:
                    self.max_y = y
                line = lines[y]
                self.max_x = len(line) - 1
                for x in range(self.max_x + 1):
                    block = line[x]
                    p = (x, y)
                    if block == '#':
                        self.edge.add(p)
                    elif block == '<':
                        self.tornado_left.add(p)
                    elif block == '>':
                        self.tornado_right.add(p)
                    elif block == '^':
                        self.tornado_up.add(p)
                    elif block == 'v':
                        self.tornado_down.add(p)
        self.end = (self.max_x - 1, self.max_y)
        self.possible_moves = lcm((self.max_x - 1), (self.max_y - 1))

    def init_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(self.size * 130, self.size * 30))

    def rc(self, c: tuple[int, int]) -> pygame.rect:
        return pygame.Rect((self.size * c[0]), (self.size * c[1]), self.size, self.size)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for p in self.edge:
             pygame.draw.rect(self.screen, (255, 255, 255), self.rc(p))

        for s in self.path:
            pygame.draw.rect(self.screen, (255, 255, 0), self.rc(s))

        pygame.display.flip()

    def get_tornadoes(self, steps_taken):
        xsiz = self.max_x - 1
        ysiz = self.max_y - 1

        tornadoes = []
        for t in self.tornado_left:
            x, y = t
            tornadoes.append((((x - 1 - steps_taken) % xsiz) + 1, y))
        for t in self.tornado_right:
            x, y = t
            tornadoes.append(((x + steps_taken - 1) % xsiz + 1, y))
        for t in self.tornado_up:
            x, y = t
            tornadoes.append((x, ((y - 1 - steps_taken) % ysiz) + 1))
        for t in self.tornado_down:
            x, y = t
            tornadoes.append((x, (y - 1 + steps_taken) % ysiz + 1))

        return tornadoes

    def get_possible_moves(self, pos: tuple[int, int], steps_taken: int):
        x, y = pos
        moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x, y)]
        tornadoes = self.get_tornadoes(steps_taken)
        filtered = []
        for m in moves:
            if m[1] < 0 or m[1] > self.max_y:
                continue
            if m in self.edge:
                continue
            if m in tornadoes:
                continue
            filtered.append(m)

        return filtered

    def shortest_path(self, start: tuple, end: tuple, blizz=0):
        queue = []
        heapq.heappush(queue, (blizz, start))
        visited = set()
        while queue:
            distance, current = heapq.heappop(queue)
            if current == end:
                print(distance)
                return distance + 1

            possible_moves = self.get_possible_moves(current, distance)
            for move in possible_moves:
                if move == end:
                    return distance

                new_distance = distance + 1
                new_blizz = new_distance % self.possible_moves
                if (move, new_blizz) in visited:
                    continue

                visited.add((move, new_blizz))
                heapq.heappush(queue, (new_distance, move))

        print(visited)
        return -1

    def find_path(self):
        first_path = self.shortest_path(self.start, self.end)
        print('part1: ', first_path)
        second_path = self.shortest_path(self.end, self.start, first_path)
        print('going back to start...', second_path)
        third_path = self.shortest_path(self.start, self.end, second_path)
        print('part2: ', third_path)


    def wait_key(self):
        while True:
            for et in pygame.event.get():
                if et.type == pygame.QUIT:
                    exit(0)

                if et.type == pygame.KEYDOWN:
                    return
            time.sleep(0.01)


def main():
    game = Game()
    game.find_path()

if __name__ == '__main__':
    main()
