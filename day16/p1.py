import functools
import networkx as nx


def main():
    with open('day16.txt') as data:
        lines = data.read().splitlines()
        flows = dict()
        valves = []
        g = nx.DiGraph()

        for line in lines:
            name = line.split('ve ')[1].split(' ')[0]
            flow = int(line.split('=')[1].split(';')[0])
            if flow > 0:
                flows[name] = flow
            valves.append(name)
            tunnels = line.split('to valve')[1][1:].strip().split(', ')
            for t in tunnels:
                g.add_edge(name, t)

        dists = nx.floyd_warshall(g)

        @functools.cache
        def find_best(opened, cycles, pos):
            best = 0
            for valve in opened:
                dist = int(dists[pos][valve])
                if dist < 1:
                    continue

                x = 0
                if dist < cycles:
                    next_cycles = cycles - dist - 1
                    x = flows[valve] * next_cycles

                    op = set(opened)
                    op.remove(valve)
                    x += find_best(frozenset(op), next_cycles, valve)
                if x > best:
                    best = x

            return best

        print(find_best(frozenset(flows), 30, 'AA'))


if __name__ == '__main__':
    main()
