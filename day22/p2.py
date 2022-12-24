import re


class Game:
    map: dict
    commands: list
    direction: 0
    topologies: dict

    def __init__(self):
        self.map = dict()
        self.topologies = dict()
        self.commands = []
        self.direction = 0
        self.position: tuple[int, int]
        self.max_x = 0
        self.max_y = 0

        with open('data.txt') as data:
            lines = data.read().splitlines()
            map_reading = True
            y = 1
            for line in lines:
                if line == '':
                    map_reading = False
                    continue

                if map_reading:
                    self.max_y = y
                    for x in range(len(line)):
                        c = line[x]
                        if x + 1 > self.max_x:
                            self.max_x = x + 1
                        if c == '.':
                            self.map[(x + 1, y)] = 0
                        elif c == '#':
                            self.map[(x + 1, y)] = 1
                    y += 1
                else:
                    self.commands = list(map(lambda s: (int(s[0]), s[1]), re.findall(r'([0-9]+)([LRX])', line)))
            self.position = list(self.map.keys())[0]
            self.create_map_topology()

    def get_quadrant(self, p) -> int:
        for q in self.topologies:
            if p[0] >= q[0] and q[1] >= p[1] >= q[2] and p[1] <= q[3]:
                return q
        raise 'Out of bounds'

    def create_map_topology(self):
        topologies = dict()
        side_len = max(self.max_y, self.max_x) // 4
        print(f"x:y {self.max_x}, {self.max_y}; side_len: {side_len}")
        side = 1
        for y in range(self.max_y // side_len):
            rline = ''
            for x in range(self.max_x // side_len):
                min_x = (x*side_len) + 1
                max_x = min_x + side_len
                min_y = (y*side_len) + 1
                max_y = y + side_len

                g = self.map.get((min_x, min_y))
                if g is None:
                    rline += '_'
                else:
                    rline += str(side)
                    topologies[side] = (min_x, max_x, min_y, max_y)
                    side += 1
            print(rline)
        self.topologies = topologies

    def go_over_edge(self, new_pos):
        x, y = new_pos
        # TODO fix these...
        if 51 <= x <= 100 and 1 <= y <= 50:
            if self.direction == 1:
                return 150, (x - 150) + 50, 3
            elif self.direction == 2:
                return 0, y + 100, 1
        elif 51 <= x <= 100 and 1 <= y <= 50:
            if self.direction == 2:
                return 50 - (x - 100), 51, 0
            elif self.direction == 3:
                return y + 50, 51, 0
        elif 51 <= x <= 100 and 1 <= y <= 50:
            if self.direction == 1:
                return (y - 50) + 150, 50, 0
            elif self.direction == 1:
                x_off = x - 100
                return 50 - x_off, 150, 0
        elif 51 <= x <= 100 and 1 <= y <= 50:
            if self.direction == 2:
                return 101, (x - 50), 1
            elif self.direction == 0:
                return 50, (x - 50) + 100, 3
        elif 51 <= x <= 100 and 1 <= y <= 50:
            if self.direction == 2:
                return 150 - x, 1, 0
            elif self.direction == 3:
                return 150 + (y - 50), 1, 0
        elif 51 <= x <= 100 and 1 <= y <= 50:
            if self.direction == 3:
                return 200, y - 101, 3
            elif self.direction == 0:
                return 150 - x, 100, 2
        else:
            print(f"{x}, {y}, {self.direction}")
            raise f'{x}, {y}'

    def check_position(self, new_pos: tuple[int, int]):
        block = self.map.get(new_pos)
        if block == 0:
            self.position = new_pos
            return

        if block == 1:
            return

        if block is None:
            x, y, d = self.go_over_edge(self.position)
            self.direction = d
            self.check_position((x, y))

    def move(self):
        if self.direction == 0:
            new_pos = (self.position[0] + 1, self.position[1])
        elif self.direction == 1:
            new_pos = (self.position[0], self.position[1] + 1)
        elif self.direction == 2:
            new_pos = (self.position[0] - 1, self.position[1])
        else:
            new_pos = (self.position[0], self.position[1] - 1)
        self.check_position(new_pos)

    def step(self, command: tuple[int, str]):
        for _ in list(range(command[0])):
            self.move()

        # rotate
        if command[1] == 'R':
            self.direction = (self.direction + 1) % 4
        elif command[1] == 'L':
            self.direction = (self.direction - 1) % 4

    def start(self):
        for command in self.commands:
            self.step(command)
        print(self.direction)
        print(self.position)


def main():
    game = Game()
    game.start()
    part1_result = game.position[0] * 4 + game.position[1] * 1000 + game.direction
    print(part1_result)


if __name__ == '__main__':
    main()
