def main():
    monkeys = dict()

    with open('test.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            ll = line.split(': ')
            monkeys[ll[0]] = ll[1]

    monkeys['root'] = monkeys['root'].replace('+', '=')
    monkeys['humn'] = '> > >'

    def calc(monk, force=False) -> int:
        if monk == 'humn' and force is False:
            return None

        instr = monkeys[monk]
        if isinstance(instr, int):
            return instr

        if ' ' not in instr:
            return int(instr)

        parts = instr.split(' ')
        a = calc(parts[0])
        b = calc(parts[2])
        if a is None or b is None:
            return None

        op = parts[1]
        if op == '+':
            return a + b
        if op == '*':
            return a * b
        if op == '/':
            return a // b
        if op == '-':
            return a - b

        return None

    print(monkeys)
    for m in monkeys:
        r = calc(m)
        if r is not None:
            monkeys[m] = r

    print(monkeys)

    def reverse(s):
        for mm in monkeys.keys():
            instr = monkeys[mm]
            if isinstance(instr, int):
                continue
            instr = instr.split(' ')

            a = instr[0]
            b = instr[2]
            op = instr[1]

            if a == s:
                reverse(mm)
                if op == '+':
                    monkeys[s] = f"{b} - {mm}"
                elif op == '-':
                    monkeys[s] = f"{b} + {mm}"
                elif op == '*':
                    monkeys[s] = f"{mm} / {b}"
                elif op == '/':
                    monkeys[s] = f"{mm} * {b}"
            elif b == s:
                reverse(mm)
                if op == '+':
                    monkeys[s] = f"{mm} - {a}"
                elif op == '-':
                    monkeys[s] = f"{a} - {mm}"
                elif op == '*':
                    monkeys[s] = f"{mm} / {a}"
                elif op == '/':
                    monkeys[s] = f"{a} / {mm}"

    reverse('humn')
    print(monkeys)

    # solve root
    parts = monkeys['root'].split(' ')
    left = monkeys[parts[0]]
    right = monkeys[parts[2]]
    if isinstance(left, int):
        monkeys[parts[2]] = left
        monkeys['root'] = left
    elif isinstance(right, int):
        monkeys[parts[0]] = right
        monkeys['root'] = right

    print(monkeys)

    for m in monkeys:
        r = calc(m)
        if r is not None:
            monkeys[m] = r

    print(monkeys)
    print(calc('humn', True))


if __name__ == '__main__':
    main()
