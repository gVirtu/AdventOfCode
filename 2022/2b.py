score = 0

ROCK = 0
PAPER = 1
SCISSORS = 2

LOSE = 0
DRAW = 1
WIN = 2

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
    DRAW: ROCK,
    LOSE: SCISSORS,
    WIN: PAPER,
  },
  PAPER: {
    WIN: SCISSORS,
    DRAW: PAPER,
    LOSE: ROCK,
  },
  SCISSORS: {
    LOSE: PAPER,
    WIN: ROCK,
    DRAW: SCISSORS,
  },
}

while True:
  try:
    line = input()
    opponentPlayChr, outcomeChr = line.split(' ')

    opponentPlay = ord(opponentPlayChr) - ord('A')
    outcome = ord(outcomeChr) - ord('X')

    yourPlay = MATCHUPS[opponentPlay][outcome]
    score += SHAPE_SCORES[yourPlay] + OUTCOME_SCORES[outcome]

  except EOFError:
    break

print(score)

