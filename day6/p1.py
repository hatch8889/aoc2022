
def has_duplicated_chars(s: str) -> bool:
    char_sum = 0
    for ch in list(s):
        for ch2 in list(s):
            if ch == ch2:
                char_sum += 1
    return char_sum > len(s)


def get_marker_index(line: str) -> int:
    for idx in list(range(0, len(line) - 3)):
        if has_duplicated_chars(line[idx:idx+4]):
            continue
        return idx + 4


def main():
    with open('day6.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            result = get_marker_index(line)
            print(result)


if __name__ == '__main__':
    main()
