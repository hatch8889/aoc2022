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


def get_connected(cube: tuple[int, int, int], cubes: list) -> int:
    sides = 0
    for a in get_adjacent(cube):
        if a in cubes:
            sides += 1
    return sides


def main():
    with open('day18.txt') as data:
        cubes = []
        lines = data.read().splitlines()
        for line in lines:
            cubes.append(tuple(map(int, line.split(','))))

        all_sides = 0
        for cube in cubes:
            all_sides += 6
            all_sides -= get_connected(cube, cubes)

        print(all_sides)


if __name__ == '__main__':
    main()
