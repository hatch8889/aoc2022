import enum


class Sign(enum.IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(enum.Enum):
    WIN = 0
    LOSE = 1
    DRAW = 2


SIGN_MAPPING = {
    'A': Sign.ROCK,
    'B': Sign.PAPER,
    'C': Sign.SCISSORS,
}


OUTCOME_MAPPING = {
    'X': Outcome.LOSE,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN
}


def get_winning_move(move: Sign) -> Sign:
    if move == Sign.ROCK:
        return Sign.PAPER
    if move == Sign.PAPER:
        return Sign.SCISSORS
    if move == Sign.SCISSORS:
        return Sign.ROCK


def get_losing_move(move: Sign) -> Sign:
    if move == Sign.ROCK:
        return Sign.SCISSORS
    if move == Sign.PAPER:
        return Sign.ROCK
    if move == Sign.SCISSORS:
        return Sign.PAPER


def get_score(line: str) -> int:
    if line == '':
        return 0

    opponent_move = SIGN_MAPPING[line[:1]]
    outcome = OUTCOME_MAPPING[line[2:]]

    if outcome == Outcome.WIN:
        return 6 + get_winning_move(opponent_move)
    elif outcome == Outcome.LOSE:
        return get_losing_move(opponent_move)
    return 3 + opponent_move


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
