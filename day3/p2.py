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
        if x in right and x not in ll:
            ll.append(x)
    return ll


def group_array(arr: [], group_size: int):
    ret = []
    for ii in range(int(len(arr) / group_size)):
        z = ii * group_size
        x = intersect(intersect(get_items(arr[z]), get_items(arr[z+1])), get_items(arr[z+2]))
        ret.append(x)
    return ret


def calc(inputs: []):
    groups = group_array(inputs, 3)
    ss = 0
    for g in groups:
        ss += sum(g)
        print(g)
    print(ss)


def main():
    with open('day3.txt') as data:
        inputs = data.read().splitlines()
        calc(inputs)


if __name__ == '__main__':
    main()
