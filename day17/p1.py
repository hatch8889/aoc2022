# (X, Y)
glyphs = {
    0: [(0, 0), (1, 0), (2, 0), (3, 0)], # ####
    1: [(0, 1), (1, 0), (1, 1), (2, 1), (1, 2)], # +
    2: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], # L
    3: [(0, 0), (0, 1), (0, 2), (0, 3)], # |
    4: [(0, 0), (1, 0), (0, 1), (1, 1)], # #
}


glyph_heights = [1, 3, 3, 4, 2]


def transpose_x(glyph: list, delta: int) -> list:
    transposed = list(map(lambda p: (p[0] + delta, p[1]), glyph))
    if max(map(lambda p: p[0], transposed)) > 6:
        # too far right
        return glyph
    if min(map(lambda p: p[0], transposed)) < 0:
        # too far left
        return glyph
    return transposed


def transpose_y(glyph: list, delta: int) -> list:
    transposed = list(map(lambda p: (p[0], p[1] + delta), glyph))
    return transposed


def is_intersecting(glyph: list[tuple[int, int]], bricks: list[tuple[int, int]]) -> bool:
    for p in glyph:
        if p in bricks:
            return True
    return False


def update_bricks(glyph: list[tuple[int, int]], bricks: list[tuple[int, int]]) -> list[tuple[int, int]]:
    update = []

    maxes = []
    for x in range(7):
        maxes.append(max(map(lambda y: y[1], filter(lambda k: k[0] == x, bricks),)))
    absolute_bottom = min(maxes)

    for b in bricks:
        if b[1] >= absolute_bottom:
            update.append(b)

    for p in glyph:
        update.append(p)
    return update


def get_top_floor(bricks: list[tuple[int, int]]) -> int:
    return max(map(lambda p: p[1], bricks))


def main():
    with open('test.txt') as data:
        commands = data.read()
        bricks: list[tuple[int, int]] = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
        c = 0
        max_commands = len(commands)
        max_glyphs = len(glyphs)
        gas_counter = 0

        # 42 - magic number for my solution; 7 for test data
        modulo = max_glyphs * max_commands * 7

        brick_start = 0
        brick_end = 0
        max_c = modulo * 2 + (1000000000000 % modulo)
        print(max_c)
        while c < max_c:
            if c % 10000 == 0:
                print((c * 100) // max_c, '%')

            # spawn glyph
            top_floor = get_top_floor(bricks)
            next_glyph = glyphs[c % max_glyphs]
            pos = top_floor + 4
            current_glyph = transpose_y(next_glyph, pos)
            # initial position is x+2
            current_glyph = transpose_x(current_glyph, 2)

            # falling down
            while True:
                next_command = commands[gas_counter % max_commands]
                if next_command == '<':
                    next_lr = transpose_x(current_glyph, -1)
                elif next_command == '>':
                    next_lr = transpose_x(current_glyph, 1)
                gas_counter += 1

                if not is_intersecting(next_lr, bricks):
                    current_glyph = next_lr

                next_down = transpose_y(current_glyph, -1)
                if is_intersecting(next_down, bricks):
                    bricks = update_bricks(current_glyph, bricks)
                    break
                # it can move down
                current_glyph = next_down

                pos -= 1

            c += 1
            if c == 2022:
                print('part1', get_top_floor(bricks))
            if c == modulo:
                brick_start = get_top_floor(bricks)
            if c == 2 * modulo:
                brick_end = get_top_floor(bricks)

        finish = get_top_floor(bricks)
        midpart_mult = (1000000000000 // modulo) - 1

        part2 = brick_start + (brick_end - brick_start) * midpart_mult + (finish - brick_end)
        print('part2: ', part2)


if __name__ == '__main__':
    main()
