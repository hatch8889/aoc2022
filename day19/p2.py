import copy
from collections import defaultdict
import re
import functools

minerals = {'ore', 'clay', 'obsidian', 'geode'}
mineral_set = {0: 'ore', 1: 'clay', 2: 'obsidian', 3: 'geode'}
maxticks = 32


def create_robot_costs(d: list):
    robot_costs = defaultdict()
    robot_costs['ore'] = defaultdict(lambda: 0)
    robot_costs['ore']['ore'] = int(d[0])
    robot_costs['clay'] = defaultdict(lambda: 0)
    robot_costs['clay']['ore'] = int(d[1])
    robot_costs['obsidian'] = defaultdict(lambda: 0)
    robot_costs['obsidian']['ore'] = int(d[2])
    robot_costs['obsidian']['clay'] = int(d[3])
    robot_costs['geode'] = defaultdict(lambda: 0)
    robot_costs['geode']['ore'] = int(d[4])
    robot_costs['geode']['obsidian'] = int(d[5])

    return robot_costs


def dict_pack(d: dict) -> int:
    f = {0: 1, 1: 300, 2: 300*300, 3: 300*300*300}
    r = 0
    for ii in range(4):
        m = mineral_set[ii]
        r += d[m] * f[ii]
    return r


def dict_unpack(n: int) -> dict:
    d = dict()
    d['ore'] = n % 300
    d['clay'] = n // 300 % 300
    d['obsidian'] = n // (300*300) % 300
    d['geode'] = n // (300*300*300) % 300
    return d


class State:
    robots: dict
    stash: dict
    robotCosts: defaultdict
    ticks: int

    def __init__(self, robot_costs: defaultdict):
        self.ticks = 0
        self.robotCosts = robot_costs
        self.robots = dict()
        self.stash = dict()
        for m in minerals:
            self.robots[m] = 0
            self.stash[m] = 0
        self.robots['ore'] = 1

    def tick(self):
        for mineral in minerals:
            self.stash[mineral] += self.robots[mineral]
        self.ticks += 1

    def evaluate(self):
        ore = self.robotCosts['ore']['ore']
        clay = self.robotCosts['clay']['ore']
        obsidian = self.robotCosts['obsidian']['clay'] * clay + self.robotCosts['obsidian']['ore']
        geode = self.robotCosts['geode']['obsidian'] * obsidian + self.robotCosts['obsidian']['ore']

        return self.robots['ore'] * ore + self.robots['clay'] * clay + self.robots['obsidian'] * obsidian + self.robots['geode'] * geode

    def robots_i_can_buy(self):
        bots = []
        for r in minerals:
            cost = self.robotCosts[r]
            can_buy = True
            for m in minerals:
                if cost[m] > self.stash[m]:
                    can_buy = False
            if can_buy:
                bots.append(r)
        return bots

    def buy_robot(self, robot: str):
        cost = self.robotCosts[robot]
        for m in minerals:
            if cost[m] > self.stash[m]:
                return False
        for m in minerals:
            self.stash[m] -= cost[m]
        self.robots[robot] += 1

        return True

    def __str__(self):
        return f"TICK: {self.ticks} Ore: {self.stash['ore']} | clay: {self.stash['clay']} | obsidian: {self.stash['obsidian']} | Geodes: {self.stash['geode']}" \
               f"  ROBOTS: Ore: {self.robots['ore']} | clay: {self.robots['clay']} | obsidian: {self.robots['obsidian']} | Geodes: {self.robots['geode']}"

    def __eq__(self, other):
        return self.id() == other.id()


def game(robot_costs):
    best_solves = defaultdict(lambda: 0)
    evals = defaultdict(lambda: 0)

    @functools.cache
    def find_best(ticks: int, stash: int, robots: int) -> int:
        global bb
        state = State(robot_costs)
        state.ticks = ticks
        state.stash = dict_unpack(stash)
        state.robots = dict_unpack(robots)

        if state.ticks == maxticks:
            return state.stash['geode']

        if state.ticks > 20:
            # give up
            if best_solves[state.ticks] > state.robots['geode']:
                return state.robots['geode']

        if state.robots['geode'] > best_solves[state.ticks]:
            print(state)
            best_solves[state.ticks] = state.robots['geode']

        if state.evaluate() >= evals[state.ticks]:
            evals[state.tick] = state.evaluate()
        else:
            return state.stash['geode']

        bots_i_can_buy = state.robots_i_can_buy()
        state.tick()
        best_result = 0
        for o in bots_i_can_buy:
            k = copy.deepcopy(state)
            k.buy_robot(o)
            res = find_best(k.ticks, dict_pack(k.stash), dict_pack(k.robots))
            if res > best_result:
                best_result = res

        if len(bots_i_can_buy) < 4:
            res = find_best(state.ticks, dict_pack(state.stash), dict_pack(state.robots))
            if res > best_result:
                best_result = res
        return best_result

    return find_best(0, 0, 1)


def main():
    with open('day19.txt') as data:
        lines = data.read().splitlines()
        s = 1
        for ii in range(0, 3):
            line = lines[ii]
            inp = re.findall(" (\d\d?) ", line)
            robot_costs = create_robot_costs(inp)
            result = game(robot_costs)
            print(f'Blueprint {ii+1} = {result}')
            s *= result
        print(s)


if __name__ == '__main__':
    main()
