import json


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


def main():
    with open('day13.txt') as data:
        pairs = []
        lines = data.read().splitlines()
        for ii in range(0, len(lines), 3):
            left = json.loads(lines[ii])
            right = json.loads(lines[ii+1])
            pairs.append((left, right))

        result = 0
        for ii in range(len(pairs)):
            pair = pairs[ii]
            o = compare(pair[0], pair[1])
            print(o)
            if o:
                result += ii + 1

        print(result)


if __name__ == '__main__':
    main()
