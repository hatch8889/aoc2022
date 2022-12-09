import math

visited = set([(0, 0)])

head_position = (0, 0)
tail_position = (0, 0)


def get_dist() -> float:
    return math.sqrt((head_position[0] - tail_position[0])**2 + (head_position[1] - tail_position[1])**2)


def move_tail():
    global tail_position
    global head_position

    # transpose head, so tail is at 0,0
    new_head = (head_position[0] - tail_position[0], head_position[1] - tail_position[1])
    if new_head[0] >= 1 and new_head[1] >= 1:
        tail_position = move(tail_position, 'D')
        tail_position = move(tail_position, 'R')
    elif new_head[0] >= 1 and new_head[1] <= -1:
        tail_position = move(tail_position, 'U')
        tail_position = move(tail_position, 'R')
    elif new_head[0] <= -1 and new_head[1] <= -1:
        tail_position = move(tail_position, 'U')
        tail_position = move(tail_position, 'L')
    elif new_head[0] <= -1 and new_head[1] >= 1:
        tail_position = move(tail_position, 'D')
        tail_position = move(tail_position, 'L')
    elif new_head[1] < -1:
        tail_position = move(tail_position, 'U')
    elif new_head[1] > 1:
        tail_position = move(tail_position, 'D')
    elif new_head[0] > 1:
        tail_position = move(tail_position, 'R')
    elif new_head[0] < -1:
        tail_position = move(tail_position, 'L')
    else:
        raise 'oops'


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
    global head_position
    global tail_position
    head_position = move(head_position, direction)

    dist = get_dist()
    if dist > 1.5:
        move_tail()
        visited.add(tail_position)


def calc(direction: str, steps: int):
    for _ in range(0, steps):
        step(direction)


def main():
    with open('day9.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            parts = line.split(' ')
            calc(parts[0], int(parts[1]))
        print(len(visited))


if __name__ == '__main__':
    main()
