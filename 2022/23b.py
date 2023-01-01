elves = set()

row = 0

INFINITY = int(10e23)

minRow = INFINITY
maxRow = -INFINITY
minCol = INFINITY
maxCol = -INFINITY

NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)

DIRECTIONS = [NORTH, SOUTH, WEST, EAST]

CHECK_POSITIONS = {
    NORTH: [(-1, 0), (-1, -1), (-1, 1)],
    SOUTH: [(1, 0), (1, -1), (1, 1)],
    WEST: [(0, -1), (-1, -1), (1, -1)],
    EAST: [(0, 1), (-1, 1), (1, 1)],
}

SURROUNDING_POSITIONS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

while True:
    try:
        line = input()

        for i in range(len(line)):
            if line[i] == "#":
                elves.add((row, i))

        row += 1

    except EOFError:
        break


def prettyPrint():
    minRow = INFINITY
    maxRow = -INFINITY
    minCol = INFINITY
    maxCol = -INFINITY

    for elf in elves:
        minRow = min(minRow, elf[0])
        maxRow = max(maxRow, elf[0])
        minCol = min(minCol, elf[1])
        maxCol = max(maxCol, elf[1])

    for i in range(minRow, maxRow + 1):
        for j in range(minCol, maxCol + 1):
            if (i, j) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def shiftedPosition(position, delta):
    return (position[0] + delta[0], position[1] + delta[1])


# prettyPrint()

for currentRound in range(INFINITY):
    proposedPositions = dict()
    bannedPositions = set()

    # print(f"ROUND {currentRound}")

    for elf in elves:
        for direction in DIRECTIONS:
            target = shiftedPosition(elf, direction)

            # Two elves already proposed moving to this position
            if target in bannedPositions:
                continue

            hasNeighbors = False
            # Check all surrounding positions to see if chooses to not move
            for offset in SURROUNDING_POSITIONS:
                if shiftedPosition(elf, offset) in elves:
                    hasNeighbors = True
                    break

            if not hasNeighbors:
                break

            # Check all neighboring positions according to the direction we're moving
            checkPassed = True
            for offset in CHECK_POSITIONS[direction]:
                checkPosition = shiftedPosition(elf, offset)
                if checkPosition in elves:
                    checkPassed = False
                    break

            if checkPassed:
                # Second elf proposing moving to a single target, ban this position for future elves
                if target in proposedPositions:
                    bannedPositions.add(target)
                    del proposedPositions[target]
                    break
                else:
                    # Check passed, first elf proposing moving to this target, all good
                    proposedPositions[target] = elf
                    break

    if not proposedPositions:
        print(currentRound + 1)
        break

    for target, elf in proposedPositions.items():
        elves.remove(elf)
        elves.add(target)

    # prettyPrint()

    # Rotate directions order
    DIRECTIONS.append(DIRECTIONS.pop(0))
