monkeys: dict = dict()


class Monkey(object):
    def __init__(self):
        self.items = []
        self.operation = ''
        self.operation_num = None
        self.test_div = 0
        self.test_true = 0
        self.test_false = 0
        self.inspections = 0

    def do_round(self):
        for item in self.items:
            self.inspections += 1
            if self.operation == '*':
                worry = item * (self.operation_num if self.operation_num else item)
            else:
                worry = item + (self.operation_num if self.operation_num else item)

            worry = worry // 3
            test = worry % self.test_div == 0
            if test:
                monkeys[self.test_true].items.append(worry)
            else:
                monkeys[self.test_false].items.append(worry)
        self.items = []

    def __str__(self):
        return 'ins: {ins} items: {items}'.format(ins=self.inspections, items=len(self.items))


def main():
    current_id = -1
    with open('day11.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            if line.startswith('Monkey '):
                current_id += 1
                monkeys[current_id] = Monkey()
            elif line.startswith('  Starting items: '):
                items = line.split('  Starting items: ')[1].split(', ')
                for item in items:
                    monkeys[current_id].items.append(int(item))
            elif line.startswith('  Operation: new = old '):
                parts = line.split('  Operation: new = old ')[1].split(' ')
                monkeys[current_id].operation = parts[0]
                if parts[1] != 'old':
                    monkeys[current_id].operation_num = int(parts[1])
            elif line.startswith('  Test: divisible by '):
                monkeys[current_id].test_div = int(line.split('  Test: divisible by ')[1])
            elif line.startswith('    If true: throw to monkey '):
                monkeys[current_id].test_true = int(line.split('    If true: throw to monkey ')[1])
            elif line.startswith('    If false: throw to monkey '):
                monkeys[current_id].test_false = int(line.split('    If false: throw to monkey ')[1])

    for jj in range(20):
        for ii in range(current_id+1):
            monkeys[ii].do_round()

    inspections = sorted(map(lambda x: x.inspections, list(monkeys.values())))
    print(inspections)
    print(inspections[-1] * inspections[-2])


if __name__ == '__main__':
    main()
