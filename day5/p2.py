class Instruction(object):
    quantity: int
    origin: int
    to: int

    def __init__(self, quantity, origin, to):
        self.quantity = quantity
        self.origin = origin
        self.to = to


def parse_state_line(state: [[]], line: str):
    max = (len(line) + 1) // 4
    for i in list(range(max)):
        box = line[(i*4)+1]
        if len(state) <= i:
            state.append([])
        if str.isalpha(box):
            state[i].insert(0, box)


def do_move(state: [[]], instr: Instruction):
    boxes = state[instr.origin][-instr.quantity:]
    state[instr.origin] = state[instr.origin][:-instr.quantity]
    state[instr.to] += boxes


def read_top(state: [[]]):
    out = ''
    for i in range(len(state)):
        out += state[i][-1]
    print(out)


def main():
    state = [[]]
    with open('day5.txt') as data:
        parse_state = 0
        inputs = data.read().splitlines()
        instructions = []
        for line in inputs:
            if line == '':
                parse_state = 1
                continue

            if parse_state == 0:
                parse_state_line(state, line)
            elif str.startswith(line, 'move'):
                parts = line.split(' ')
                instructions.append(Instruction(quantity=int(parts[1]), origin=int(parts[3])-1, to=int(parts[5])-1))

        for instr in instructions:
            do_move(state, instr)

        print(state)
        read_top(state)


if __name__ == '__main__':
    main()
