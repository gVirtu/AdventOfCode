import re
from collections import defaultdict

RESOURCE_TYPE_COUNT = 4
TIME_LIMIT = 24

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

blueprints = []


class Blueprint(object):
    def __init__(self, costs) -> None:
        self.costs = costs

    def __repr__(self) -> str:
        return self.costs.__repr__()


class State(object):
    def __init__(self, time, resources, robots):
        self.time = time
        self.resources = resources
        self.robots = robots
        self.log = ""

    def __repr__(self):
        return f"At minute {self.time} - ROBOTS: f{self.robots} - RESOURCES: f{self.resources}"

    def generateResources(self):
        for i in range(RESOURCE_TYPE_COUNT):
            self.resources[i] += self.robots[i]

    def canBuild(self, blueprint, resource):
        for i in range(RESOURCE_TYPE_COUNT):
            if self.resources[i] < blueprint.costs[resource][i]:
                return False
        return True

    def buildRobot(self, blueprint, resource):
        for i in range(RESOURCE_TYPE_COUNT):
            self.resources[i] -= blueprint.costs[resource][i]
        self.robots[resource] += 1

    def advanceTime(self):
        self.time += 1

    def copy(self):
        resources = [resource for resource in self.resources]
        robots = [robot for robot in self.robots]
        newState = State(self.time, resources, robots)
        newState.log = self.log

        return newState

    def hasAdvantage(self, bestResources):
        for i in range(RESOURCE_TYPE_COUNT):
            if self.resources[i] > bestResources[i][(self.time, tuple(self.robots))]:
                return True
        return False


PATTERN = re.compile(
    "".join(
        [
            "Blueprint [0-9]+: ",
            "Each ore robot costs (?P<oreRobotOreCost>[0-9]+) ore. ",
            "Each clay robot costs (?P<clayRobotOreCost>[0-9]+) ore. ",
            "Each obsidian robot costs (?P<obsidianRobotOreCost>[0-9]+) ore and (?P<obsidianRobotClayCost>[0-9]+) clay. ",
            "Each geode robot costs (?P<geodeRobotOreCost>[0-9]+) ore and (?P<geodeRobotObsidianCost>[0-9]+) obsidian.",
        ]
    )
)

while True:
    try:
        line = input()

        lineMatch = re.search(PATTERN, line)
        assert lineMatch is not None
        blueprintData = lineMatch.groupdict()

        costs = [
            [0 for _ in range(RESOURCE_TYPE_COUNT)] for _ in range(RESOURCE_TYPE_COUNT)
        ]

        costs[ORE][ORE] = int(blueprintData["oreRobotOreCost"])
        costs[CLAY][ORE] = int(blueprintData["clayRobotOreCost"])
        costs[OBSIDIAN][ORE] = int(blueprintData["obsidianRobotOreCost"])
        costs[OBSIDIAN][CLAY] = int(blueprintData["obsidianRobotClayCost"])
        costs[GEODE][ORE] = int(blueprintData["geodeRobotOreCost"])
        costs[GEODE][OBSIDIAN] = int(blueprintData["geodeRobotObsidianCost"])

        blueprint = Blueprint(costs)

        blueprints.append(blueprint)

    except EOFError:
        break

qualityLevelSum = 0

for blueprintId, blueprint in enumerate(blueprints, 1):
    bestGeodes = 0
    bestResources = [defaultdict(int) for _ in range(RESOURCE_TYPE_COUNT)]
    queue = []

    resources = [0 for _ in range(RESOURCE_TYPE_COUNT)]
    robots = [0 for _ in range(RESOURCE_TYPE_COUNT)]
    robots[ORE] = 1

    queue.append(State(1, resources, robots))

    while queue:
        state = queue.pop(-1)

        for i in range(RESOURCE_TYPE_COUNT):
            key = (state.time, tuple(state.robots))
            bestResources[i][key] = max(state.resources[i], bestResources[i][key])

        canBuildRobot = [False for _ in range(RESOURCE_TYPE_COUNT)]

        for i in range(RESOURCE_TYPE_COUNT):
            canBuildRobot[i] = state.canBuild(blueprint, i)

        state.generateResources()
        state.advanceTime()
        if state.time <= TIME_LIMIT and state.hasAdvantage(bestResources):
            queue.append(state)

        bestGeodes = max(bestGeodes, state.resources[GEODE])

        for i in range(RESOURCE_TYPE_COUNT):
            if canBuildRobot[i]:
                newState = state.copy()
                newState.buildRobot(blueprint, i)
                newState.log = (
                    newState.log
                    + f"\n - Build {i} at time {state.time} with {state.resources}"
                )
                if newState.time <= TIME_LIMIT and newState.hasAdvantage(bestResources):
                    queue.append(newState)

    qualityLevelSum += blueprintId * bestGeodes

print(qualityLevelSum)
