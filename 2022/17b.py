from collections import defaultdict

class State:
  def __init__(self, jetPattern):
    self.SHAPES = [
      [[*'@@@@']],

      [[*'.@.'],
       [*'@@@'],
       [*'.@.']],

      [[*'..@'],
       [*'..@'],
       [*'@@@']],

      [[*'@'],
       [*'@'],
       [*'@'],
       [*'@']],

      [[*'@@'],
       [*'@@']]
    ]

    self.MAX_HEIGHT = 500000

    self.FALLING_ROCK = '@'
    self.WALL = '#'
    self.AIR = '.'

    self.LEFT = '<'
    self.RIGHT = '>'

    self.cave = [[*'#.......#'] for _ in range(self.MAX_HEIGHT)]
    self.cave[-1] = [*'#########']

    self.spawnX = 3
    self.spawnYPadding = 4
    self.spawnY = self.MAX_HEIGHT - 1 - self.spawnYPadding

    self.activeTiles = []
    self.jetPattern = [*jetPattern]

    self.currentShape = 0
    self.currentJet = 0

    self.lastShapeDeltaX = 0
    self.lastHeight = 0
    self.shapeCount = 0
    self.memo = defaultdict(list)
    self.heightIncreases = []

    self.foundCycle = False
    self.cycleStart = None
    self.cycleLength = None

  def print(self):
    for i in range(self.spawnY - 3, self.MAX_HEIGHT):
      print(''.join(self.cave[i]))

  def incrementShape(self):
    self.currentShape = (self.currentShape + 1) % len(self.SHAPES)
    self.shapeCount += 1

  def spawnShape(self):
    shape = self.SHAPES[self.currentShape]
    shapeHeight = len(shape)
    shapeWidth = len(shape[0])

    for i in range(shapeHeight):
      for j in range(shapeWidth):
        caveY = self.spawnY - (shapeHeight - 1) + i
        caveX = self.spawnX + j
        self.cave[caveY][caveX] = shape[i][j]

        if shape[i][j] == self.FALLING_ROCK:
          self.activeTiles.append((caveY, caveX))

    self.incrementShape()

  def collisionCheck(self, delta):
    for (i, j) in self.activeTiles:
      if self.cave[i + delta[0]][j + delta[1]] == self.WALL:
        return True

    return False

  def moveShape(self, delta):
    for (i, j) in self.activeTiles:
      self.cave[i][j] = self.AIR

    for index, (i, j) in enumerate(self.activeTiles):
      self.cave[i + delta[0]][j + delta[1]] = self.FALLING_ROCK
      self.activeTiles[index] = (i + delta[0], j + delta[1])

  def setShapeToRest(self):
    for (i, j) in self.activeTiles:
      self.cave[i][j] = self.WALL
      self.spawnY = min(self.spawnY, i - self.spawnYPadding)

    self.activeTiles = []

  def nextMovementDelta(self):
    movement = self.jetPattern[self.currentJet % len(self.jetPattern)]
    self.currentJet += 1

    return (0, 1) if movement == self.RIGHT else (0, -1)

  def simulateShape(self):
    self.lastShapeDeltaX = 0
    while True:
      delta = self.nextMovementDelta()

      if not self.collisionCheck(delta):
        self.moveShape(delta)
        self.lastShapeDeltaX += delta[1]

      fallDelta = (1, 0)

      if self.collisionCheck(fallDelta):
        self.setShapeToRest()
        break
      else:
        self.moveShape(fallDelta)

  def getTowerHeight(self):
    return (self.MAX_HEIGHT - 1) - (self.spawnY + self.spawnYPadding)

  def memoize(self):
    heightNow = self.getTowerHeight()
    heightIncrease = heightNow - self.lastHeight
    self.lastHeight = heightNow

    self.heightIncreases.append(heightIncrease)

    key = (
      self.currentJet % len(self.jetPattern),
      self.currentShape % len(self.SHAPES),
      self.lastShapeDeltaX
    )

    value = (self.shapeCount, heightIncrease)

    self.memo[key].append(value)

    if len(self.memo[key]) > 3 \
      and self.memo[key][-1][1] == self.memo[key][-2][1] \
      and self.memo[key][-1][1] == self.memo[key][-3][1]:
      self.cycleStart = self.memo[key][-2][0]
      self.cycleLength = self.shapeCount - self.cycleStart
      self.foundCycle = True


def simulate(state:State, maxRocks, target):
  for _ in range(maxRocks):
    state.spawnShape()
    state.simulateShape()
    state.memoize()

    if state.foundCycle:
      print(state.heightIncreases)
      print(f'Found cycle starting at {state.cycleStart}, of size {state.cycleLength}')

      startIncreases = \
        state.heightIncreases[:state.cycleStart]
      startSum = sum([inc for inc in startIncreases])
      print(f'Start sum = {startSum}')

      cycleHeightIncreases = \
        state.heightIncreases[state.cycleStart:state.cycleStart+state.cycleLength]
      cycleSum = sum([inc for inc in cycleHeightIncreases])
      cycleTimes = (target - state.cycleStart) // state.cycleLength
      print(f'Cycle sum = {cycleSum}')
      print(f'Cycle times = {cycleTimes}')

      remainder = (target - state.cycleStart) % state.cycleLength
      print(f'Remainder = {remainder}')

      remainderIncreases = \
        state.heightIncreases[state.cycleStart:state.cycleStart+remainder]
      remainderSum = sum([inc for inc in remainderIncreases])
      print(f'Remainder sum = {remainderSum}')

      total = startSum + (cycleTimes * cycleSum) + remainderSum
      print(total)

      break

jetPattern = input()

state = State(jetPattern)
simulate(state, 100000, 1000000000000)
