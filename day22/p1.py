import re


class Game:
    map: dict
    commands: list
    direction: 0

    def __init__(self):
        self.map = dict()
        self.commands = []
        self.direction = 0
        self.position: tuple[int, int]

        with open('data.txt') as data:
            lines = data.read().splitlines()
            map_reading = True
            y = 1
            for line in lines:
                if line == '':
                    map_reading = False
                    continue

                if map_reading:
                    for x in range(len(line)):
                        c = line[x]
                        if c == '.':
                            self.map[(x + 1, y)] = 0
                        elif c == '#':
                            self.map[(x + 1, y)] = 1
                    y += 1
                else:
                    self.commands = list(map(lambda s: (int(s[0]), s[1]), re.findall(r'([0-9]+)([LRX])', line)))
            self.position = list(self.map.keys())[0]

    def check_position(self, new_pos: tuple[int, int]):
        block = self.map.get(new_pos)
        if block == 0:
            self.position = new_pos
            return

        if block == 1:
            return

        if block is None:
            keys = self.map.keys()
            # wrap around, try again
            if self.direction == 0:
                check_pos = list(filter(lambda p: p[1] == new_pos[1], keys))[0]
                self.check_position(check_pos)
                return
            elif self.direction == 1:
                check_pos = list(filter(lambda p: p[0] == new_pos[0], keys))[0]
                self.check_position(check_pos)
                return
            elif self.direction == 2:
                check_pos = list(filter(lambda p: p[1] == new_pos[1], keys))[-1]
                self.check_position(check_pos)
                return
            elif self.direction == 3:
                check_pos = list(filter(lambda p: p[0] == new_pos[0], keys))[-1]
                self.check_position(check_pos)
                return

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
