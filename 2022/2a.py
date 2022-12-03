score = 0

ROCK = 0
PAPER = 1
SCISSORS = 2

WIN = 0
DRAW = 1
LOSE = 2

SHAPE_SCORES = {
  ROCK: 1,
  PAPER: 2,
  SCISSORS: 3
}

OUTCOME_SCORES = {
  WIN: 6,
  DRAW: 3,
  LOSE: 0
}

MATCHUPS = {
  ROCK: {
    ROCK: DRAW,
    PAPER: LOSE,
    SCISSORS: WIN,
  },
  PAPER: {
    ROCK: WIN,
    PAPER: DRAW,
    SCISSORS: LOSE,
  },
  SCISSORS: {
    ROCK: LOSE,
    PAPER: WIN,
    SCISSORS: DRAW,
  },
}

while True:
  try:
    line = input()
    opponentPlayChr, yourPlayChr = line.split(' ')

    opponentPlay = ord(opponentPlayChr) - ord('A')
    yourPlay = ord(yourPlayChr) - ord('X')

    outcome = MATCHUPS[yourPlay][opponentPlay]
    score += SHAPE_SCORES[yourPlay] + OUTCOME_SCORES[outcome]

  except EOFError:
    break

print(score)
