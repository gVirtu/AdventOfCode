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

    self.MAX_HEIGHT = 5000

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

  def print(self):
    for i in range(self.spawnY - 3, self.MAX_HEIGHT):
      print(''.join(self.cave[i]))

  def incrementShape(self):
    self.currentShape = (self.currentShape + 1) % len(self.SHAPES)

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
    while True:
      delta = self.nextMovementDelta()

      if not self.collisionCheck(delta):
        self.moveShape(delta)

      fallDelta = (1, 0)

      if self.collisionCheck(fallDelta):
        self.setShapeToRest()
        break
      else:
        self.moveShape(fallDelta)

  def getTowerHeight(self):
    return (self.MAX_HEIGHT - 1) - (self.spawnY + self.spawnYPadding)


def simulate(state:State, maxRocks):
  for _ in range(maxRocks):
    state.spawnShape()
    state.simulateShape()
    # state.print()

jetPattern = input()

state = State(jetPattern)
simulate(state, 2022)

print(state.getTowerHeight())
