import networkx as nx
import networkx.exception

snake = 'SabcdefghijklmnopqrstuvwxyzEX'


def get_moves(lines: list[str], pos: tuple[int, int]) -> list[tuple[int, int]]:
    max_y = len(lines)
    max_x = len(lines[0])
    moves = []
    current_letter = snake.index(lines[pos[0]][pos[1]])

    if pos[0] > 0:
        ltr = snake.index(lines[pos[0] - 1][pos[1]])
        if ltr <= current_letter + 1:
            moves.append((pos[0] - 1, pos[1]))
    if pos[1] > 0:
        ltr = snake.index(lines[pos[0]][pos[1] - 1])
        if ltr <= current_letter + 1:
            moves.append((pos[0], pos[1] - 1))
    if pos[0] + 1 < max_y:
        ltr = snake.index(lines[pos[0] + 1][pos[1]])
        if ltr <= current_letter + 1:
            moves.append((pos[0] + 1, pos[1]))
    if pos[1] + 1 < max_x:
        ltr = snake.index(lines[pos[0]][pos[1] + 1])
        if ltr <= current_letter + 1:
            moves.append((pos[0], pos[1] + 1))

    return moves


def main():
    with open('day12.txt') as data:
        lines = data.read().splitlines()
        max_y = len(lines)
        max_x = len(lines[0])
        G = nx.DiGraph()
        start: tuple[int, int]
        end: tuple[int, int]
        possible_alternative_starts = []

        for y in range(max_y):
            for x in range(max_x):
                if lines[y][x] == 'S':
                    start = (y, x)

                if lines[y][x] == 'E':
                    end = (y, x)

                if lines[y][x] == 'a':
                    possible_alternative_starts.append((y, x))

                G.add_node((y, x), ltr=lines[y][x])
                moves = get_moves(lines, (y, x))
                for move in moves:
                    G.add_edge((y, x), move)

        path = nx.shortest_path(G, start, end)
        print('Part 1:')
        print(len(path) - 1)

        paths = []
        for a in possible_alternative_starts:
            try:
                path = nx.shortest_path(G, a, end)
                paths.append(len(path))
            except networkx.exception.NetworkXNoPath:
                pass

        print('Part 2:')
        print(sorted(paths)[0] - 1)


if __name__ == '__main__':
    main()
