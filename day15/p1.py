import re
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


def main():
    with open('day15.txt') as data:
        lines = data.read().splitlines()
        a = []
        for line in lines:
            cd = re.findall(r'=([-?\d]*)', line)
            a.append(Entry(cd))

        tree = intervaltree.IntervalTree()
        for x in a:
            r = x.range_at_y(2000000)
            if r is not None:
                print(r)
                tree.appendi(r[0], r[1] + 1)

        tree.merge_overlaps(strict=True)
        s = 0
        for t in tree:
            print(t)
            s += t.end - t.begin - 1
        print(s)


if __name__ == '__main__':
    main()
