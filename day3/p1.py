from typing import List


def get_items(items: str) -> List[int]:
    ll: List[int] = []
    for c in items:
        if c.isupper():
            ll.append(ord(c) - 64 + 26)
        else:
            ll.append(ord(c) - 96)
    return ll


def intersect(left: List[int], right: List[int]):
    ll: List[int] = []
    for x in left:
        if x in right:
            if x not in ll:
                ll.append(x)
    return ll


def calc(inputs: []):
    all = []
    for rucksack in inputs:
        if rucksack == '':
            continue
        compartment_len = int(len(rucksack) / 2)

        if len(rucksack) % 2 != 0:
            print('Wrong input')
            return

        left = get_items(rucksack[:compartment_len])
        right = get_items(rucksack[-1*compartment_len:])
        out = intersect(left, right)
        print(out)
        all.append(sum(out))

    print(sum(all))


def main():
    with open('day3.txt') as data:
        inputs = data.read().splitlines()
        calc(inputs)


if __name__ == '__main__':
    main()
