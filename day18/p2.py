from collections import deque


def get_adjacent(cube: tuple[int, int, int]) -> list:
    x, y, z = cube
    return [
        (x-1, y, z),
        (x+1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1),
    ]


def get_connected(pos: tuple[int, int, int], cubes: list) -> (int, list):
    sides = 0
    adj = get_adjacent(pos)
    for a in adj:
        if a in cubes:
            sides += 1
    return sides


def part2(cubes: list):
    min = -2
    max = 22

    def is_in_bounds(pp: tuple[int, int, int]) -> bool:
        xx, yy, zz = pp
        if xx < min or yy < min or zz < min or xx > max or yy > max or zz > max:
            return False
        return True

    visited = set()
    queue = deque({(min, min, min)})
    # flood fill from outside
    while queue:
        p = queue.pop()
        if p in visited:
            continue
        visited.add(p)
        for a in get_adjacent(p):
            if a not in cubes and is_in_bounds(a):
                queue.append(a)

    n = 0
    for p in visited:
        n += get_connected(p, cubes)
    print(n)


def main():
    with open('day18.txt') as data:
        cubes = []
        lines = data.read().splitlines()
        for line in lines:
            cubes.append(tuple(map(int, line.split(','))))

        part2(cubes)


if __name__ == '__main__':
    main()
