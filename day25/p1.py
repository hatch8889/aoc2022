conv = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}


def calc(ll: list):
    for c in ll:
        s = 0
        for p in range(0, len(c)):
            z = len(c) - p - 1
            s += conv[c[p]] * (5**z)
        yield s


def main():
    with open('data.txt') as data:
        inputs = data.read().splitlines()
        val = sum(calc(inputs))
        print(val)
        result = ''
        while val:
            result = '012=-'[val % 5] + result
            if val > 2:
                val += 2
            val = val // 5
        print(result)


if __name__ == '__main__':
    main()
