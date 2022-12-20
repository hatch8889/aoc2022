def main():
    with open('test.txt') as data:
        def part2(s: str) -> int:
            return int(s) * 811589153

        initial = list(map(part2, data.read().splitlines()))
        set_len = len(initial)

        mixer = list(range(set_len))
        for _ in range(10):
            for ii in range(set_len):
                delta = initial[ii]
                if delta == 0:
                    continue

                if abs(delta) % set_len == 0:
                    continue

                index_to_change = mixer.index(ii)
                new_index = (index_to_change + delta + set_len - 1) % (set_len - 1)

                item = mixer.pop(index_to_change)
                if new_index == 0:
                    mixer.append(item)
                else:
                    mixer.insert(new_index, item)

        wooter = list(map(lambda x: initial[x], mixer))
        print(wooter)

        index_of_0 = wooter.index(0)
        i1 = wooter[mixer[(index_of_0 + 1000) % set_len]]
        i2 = wooter[mixer[(index_of_0 + 2000) % set_len]]
        i3 = wooter[mixer[(index_of_0 + 3000) % set_len]]
        print(i1, i2, i3)
        print(i1+i2+i3)


if __name__ == '__main__':
    main()
