from typing import List


def get_sections(input: str) -> List[int]:
    start = input.split('-')[0]
    end = input.split('-')[1]
    return list(range(int(start), int(end) + 1))


def parse_line(line: str) -> (List[int], List[int]):
    a = line.split(',')[0]
    b = line.split(',')[1]
    return get_sections(a), get_sections(b)


def is_intersecting(a: List[int], b: List[int]) -> bool:
    for x in a:
        if x not in b:
            return False
    return True


def calc(lines: []):
    ret = 0
    for line in lines:
        if line == '':
            break
        a, b = parse_line(line)
        if is_intersecting(a, b) or is_intersecting(b, a):
            ret += 1
    print(ret)


def main():
    with open('day4.txt') as data:
        inputs = data.read().splitlines()
        calc(inputs)


if __name__ == '__main__':
    main()
