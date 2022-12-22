def main():
    monkeys = dict()

    with open('day21.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            ll = line.split(': ')
            monkeys[ll[0]] = ll[1]

    def calc(monk) -> int:
        instr = monkeys[monk]

        if len(instr) < 4:
            return int(instr)

        parts = instr.split(' ')
        a = calc(parts[0])
        b = calc(parts[2])
        op = parts[1]
        if op == '+':
            return a + b
        if op == '*':
            return a * b
        if op == '/':
            return a // b
        if op == '-':
            return a - b

    print(calc('root'))


if __name__ == '__main__':
    main()
