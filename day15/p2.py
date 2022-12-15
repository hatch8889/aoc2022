import re
import multiprocessing

import intervaltree


def m_dist(p1, p2):
    distance = 0
    for x1, x2 in zip(p1, p2):
        distance += abs(x2 - x1)

    return distance


class Entry:
    dist: int
    s: tuple[int, int]
    b: tuple[int, int]

    def __init__(self, t: list[str]):
        self.s = (int(t[0]), int(t[1]))
        self.b = (int(t[2]), int(t[3]))
        self.dist = m_dist(self.s, self.b)

    def range_at_y(self, y: int):
        max_y = self.s[1] + self.dist
        min_y = self.s[1] - self.dist
        if y > max_y:
            return None
        if y < min_y:
            return None

        dy = 0
        if y >= self.s[1]:
            dy = max_y - y
        elif y <= self.s[1]:
            dy = y - min_y

        min_x = self.s[0] - dy
        max_x = self.s[0] + dy
        return min_x, max_x


mx = 4000000
max_cpus = 24

processes = []


def do_work(a, cpu_n):
    for y in range(cpu_n, mx, max_cpus):
        tree = intervaltree.IntervalTree()
        for x in a:
            r = x.range_at_y(y)
            if r is not None:
                min_x = r[0] if r[0] > 0 else 0
                max_x = r[1] if r[1] <= mx else mx
                if min_x == 0 and max_x == mx:
                    continue
                tree.appendi(min_x, max_x + 1)

        tree.merge_overlaps(strict=True)
        s = 0
        for t in tree:
            s += t.end - t.begin - 1
        if y % 100000 == 0:
            print(y)
        if s < mx:
            print(y)
            print('part2 result:')
            print(list(tree[0])[0][1] * mx + y)
            for p in processes:
                p.terminate()
            exit(0)

    return None, None


def main():

    with open('day15.txt') as data:
        lines = data.read().splitlines()
        a = []
        for line in lines:
            cd = re.findall(r'=([-?\d]*)', line)
            a.append(Entry(cd))

        for cpu_n in range(0, max_cpus):
            p = multiprocessing.Process(target=do_work, kwargs={'a': a, 'cpu_n': cpu_n})
            p.start()
            processes.append(p)

        for p in processes:
            p.join()


if __name__ == '__main__':
    main()
