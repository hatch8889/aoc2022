import json
from functools import cmp_to_key


def get_pairs(left, right) -> list:
    o = []
    for ii in range(max(len(left), len(right))):
        le = left[ii] if ii < len(left) else None
        ri = right[ii] if ii < len(right) else None
        o.append((le, ri))
    return o


def compare(left, right):
    if left is None:
        return True
    if right is None:
        return False

    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        elif left < right:
            return True
        else:
            return None

    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

    for pair in get_pairs(left, right):
        o = compare(pair[0], pair[1])
        if o is not None:
            return o
    return None


def cz(left, right):
    return -1 if compare(left, right) is True else False


def main():
    with open('day13.txt') as data:
        all_input = []
        lines = data.read().splitlines()
        for line in lines:
            if line == '':
                continue
            all_input.append(json.loads(line))

        all_input.append(json.loads('[[2]]'))
        all_input.append(json.loads('[[6]]'))

        sor = sorted(all_input, key=cmp_to_key(cz))

        a = 0
        b = 0
        for ii in range(len(sor)):
            pair = sor[ii]
            if str(pair) == '[[2]]':
                a = ii + 1
            if str(pair) == '[[6]]':
                b = ii + 1

        print(a*b)


if __name__ == '__main__':
    main()
