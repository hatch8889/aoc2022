def calc(inputs):
    s = 0
    all_sums = []
    for x in inputs:
        if x == '':
            all_sums.append(s)
            s = 0
        else:
            s += int(x)

    print(sorted(all_sums)[-3:])
    print(sum(sorted(all_sums)[-3:]))


def main():
    with open('day1.txt') as data:
        inputs = data.read().splitlines()
        calc(inputs)


if __name__ == '__main__':
    main()
