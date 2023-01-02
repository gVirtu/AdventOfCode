POWERS = [5**i for i in range(20)]
SNAFU_CHARS = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

REPLACEMENTS = ["1", "0", "-", "="]

snafuNumbers = []

while True:
    try:
        line = input()
        snafuNumbers.append(line)

    except EOFError:
        break


def snafuToNumber(snafu):
    result = 0

    for i, char in enumerate(snafu):
        c = SNAFU_CHARS[char]
        n = len(snafu) - 1 - i
        result += POWERS[n] * c

    return result


def maxSnafuNumberByDigitCount(digits):
    return 2 * sum(POWERS[:digits])


def numberToSnafu(number):
    digits = 0
    while number > maxSnafuNumberByDigitCount(digits):
        digits += 1

    current = maxSnafuNumberByDigitCount(digits)
    currentString = ["2" for _ in range(digits)]

    for i in range(digits - 1, -1, -1):
        for j in range(len(REPLACEMENTS)):
            if number <= current - POWERS[i]:
                current -= POWERS[i]
                currentString[i] = REPLACEMENTS[j]
            if number == current:
                break

    return "".join(reversed(currentString))


summation = sum(snafuToNumber(x) for x in snafuNumbers)
print(numberToSnafu(summation))
