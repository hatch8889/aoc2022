import enum


class Sign(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


SIGN_MAPPING = {
    'A': Sign.ROCK,
    'B': Sign.PAPER,
    'C': Sign.SCISSORS,
    'X': Sign.ROCK,
    'Y': Sign.PAPER,
    'Z': Sign.SCISSORS,
}


def get_score(line: str) -> int:
    if line == '':
        return 0
    # A Y
    opponent_move = SIGN_MAPPING[line[:1]]
    my_move = SIGN_MAPPING[line[2:]]
    if opponent_move == my_move:
        # draw
        return 3 + my_move.value

    if opponent_move == Sign.ROCK and my_move == Sign.SCISSORS:
        # lose
        return 0 + my_move.value

    if my_move.value > opponent_move.value or (my_move == Sign.ROCK and opponent_move == Sign.SCISSORS):
        # win
        return 6 + my_move.value

    # lose
    return 0 + my_move.value


def calc(inputs):
    results = []
    for line in inputs:
        results.append(get_score(line))

    print(sum(results))


def main():
    with open('day2.txt') as data:
        inputs = data.read().splitlines()
        calc(inputs)


if __name__ == '__main__':
    main()
