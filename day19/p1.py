import copy
from collections import defaultdict
from queue import PriorityQueue
import re

minerals = {'ore', 'clay', 'obsidian', 'geode'}
maxticks = 24


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


class State:
    robots: dict
    stash: dict
    robotCosts: defaultdict
    ticks: int
    ore_spent: int

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
        clay = self.robotCosts['clay']['ore']
        obsidian = self.robotCosts['obsidian']['clay'] * clay + self.robotCosts['obsidian']['ore']
        geode = self.robotCosts['geode']['obsidian'] * obsidian + self.robotCosts['obsidian']['ore']

        return self.stash['ore'] + self.stash['clay'] * clay + self.stash['obsidian'] * obsidian + self.stash['geode'] * geode

    def robots_i_can_buy(self):
        bots = []
        for r in minerals:
            cost = self.robotCosts[r]
            can_buy = True
            for m in list(reversed(list(minerals))):
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

    def __lt__(self, other):
        return self.evaluate() > other.evaluate()


def game(robot_costs):
    pq = PriorityQueue()
    pq.put((0, State(robot_costs)))
    best_solves = defaultdict(lambda: 0)

    best_solve = -1
    best_state = None

    def smart_append(state: State):
        ev = state.evaluate() * -1
        pq.put((ev, state))

    while not pq.empty():
        prio, state = pq.get()
        bots_i_can_buy = state.robots_i_can_buy()
        state.tick()

        if state.evaluate() >= best_solves[state.ticks]:
            best_solves[state.ticks] = state.evaluate()
        elif state.evaluate() < best_solves[state.ticks] - 200:
            continue

        if state.ticks == maxticks:
            if state.stash['geode'] > best_solve:
                best_solve = state.stash['geode']
                best_state = state
            continue

        ### create robots
        for o in bots_i_can_buy:
            k = copy.deepcopy(state)
            k.buy_robot(o)
            smart_append(k)
        if len(bots_i_can_buy) < 4:
            smart_append(state)

    print(best_state)
    return best_solve


def main():
    with open('day19.txt') as data:
        lines = data.read().splitlines()
        s = 0
        for ii in range(len(lines)):
            line = lines[ii]
            inp = re.findall(" (\d\d?) ", line)
            robot_costs = create_robot_costs(inp)
            result = game(robot_costs)
            print(f'Blueprint {ii+1} = {result}')
            s += result * (ii+1)
        print(s)


if __name__ == '__main__':
    main()
