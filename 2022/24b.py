# Grid will contain T copies of W x H tiles,
# where W and H are the input dimensions and
# T is the total number of unique blizzard
# configurations, given the the LCM of W and H.
grid = [[]]

EMPTY = 0
WALL = 1
LEFT_BLIZZARD = 2
UP_BLIZZARD = 4
RIGHT_BLIZZARD = 8
DOWN_BLIZZARD = 16

TILE_CHARS = {
    "#": WALL,
    ".": EMPTY,
    "<": LEFT_BLIZZARD,
    ">": RIGHT_BLIZZARD,
    "^": UP_BLIZZARD,
    "v": DOWN_BLIZZARD,
}

CHARS_MAP = {v: k for k, v in TILE_CHARS.items()}


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b


def prettyPrint(grid):
    for epoch in grid:
        print("=======================")

        for row in epoch:
            for cell in row:
                if cell in CHARS_MAP:
                    print(CHARS_MAP[cell], end="")
                else:
                    print("2", end="")

            print("")


row = 0
while True:
    try:
        line = input()

        grid[0].append([])

        for char in line:
            grid[0][row].append(TILE_CHARS[char])

        row += 1

    except EOFError:
        break

rows = len(grid[0])
columns = len(grid[0][0])

GOAL = (rows - 1, columns - 2)

epochs = int(lcm(rows - 2, columns - 2))  # Exclude the outer walls

for e in range(1, epochs):
    grid.append([])
    grid[e].append(grid[e - 1][0])

    for i in range(1, rows - 1):
        grid[e].append([WALL])

        for j in range(1, columns - 1):
            left = j - 1 if j > 1 else columns - 2
            right = j + 1 if j < columns - 2 else 1
            up = i - 1 if i > 1 else rows - 2
            down = i + 1 if i < rows - 2 else 1

            value = EMPTY
            value |= LEFT_BLIZZARD if grid[e - 1][i][right] & LEFT_BLIZZARD else 0
            value |= RIGHT_BLIZZARD if grid[e - 1][i][left] & RIGHT_BLIZZARD else 0
            value |= UP_BLIZZARD if grid[e - 1][down][j] & UP_BLIZZARD else 0
            value |= DOWN_BLIZZARD if grid[e - 1][up][j] & DOWN_BLIZZARD else 0

            grid[e][i].append(value)

        grid[e][i].append(WALL)

    grid[e].append(grid[e - 1][-1])


def timeToGoal(fromPoint, toPoint, startEpoch):
    global grid, rows, columns

    queue = []
    queue.append((startEpoch, fromPoint[0], fromPoint[1], 0))
    visited = set()

    while queue:
        e, i, j, t = queue.pop(0)

        if (i, j) == toPoint:
            return t, e

        nextE = (e + 1) % epochs

        # Move down
        if (
            i < rows - 1
            and grid[nextE][i + 1][j] == EMPTY
            and (nextE, i + 1, j) not in visited
        ):
            queue.append((nextE, i + 1, j, t + 1))
            visited.add((nextE, i + 1, j))

        # Move up
        if (
            i > 0
            and grid[nextE][i - 1][j] == EMPTY
            and (nextE, i - 1, j) not in visited
        ):
            queue.append((nextE, i - 1, j, t + 1))
            visited.add((nextE, i - 1, j))

        # Move right
        if grid[nextE][i][j + 1] == EMPTY and (nextE, i, j + 1) not in visited:
            queue.append((nextE, i, j + 1, t + 1))
            visited.add((nextE, i, j + 1))

        # Move left
        if grid[nextE][i][j - 1] == EMPTY and (nextE, i, j - 1) not in visited:
            queue.append((nextE, i, j - 1, t + 1))
            visited.add((nextE, i, j - 1))

        # Wait in place
        if grid[nextE][i][j] == EMPTY and (nextE, i, j) not in visited:
            queue.append((nextE, i, j, t + 1))
            visited.add((nextE, i, j))

    return None, None


firstRun, endEpoch = timeToGoal((0, 1), GOAL, 0)
secondRun, endEpoch = timeToGoal(GOAL, (0, 1), endEpoch)
thirdRun, _ = timeToGoal((0, 1), GOAL, endEpoch)

assert firstRun is not None
assert secondRun is not None
assert thirdRun is not None

print(firstRun + secondRun + thirdRun)
