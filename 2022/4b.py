overlapCount = 0

def overlaps(a, b):
    return (
        (b[0] <= a[0] <= b[1])
        or (b[0] <= a[1] <= b[1])
        or (a[0] <= b[0] and a[1] >= b[1])
    )

while True:
    try:
        line = input()
        aString, bString = line.split(",")

        a = tuple(map(int, aString.split("-")))
        b = tuple(map(int, bString.split("-")))

        if overlaps(a, b):
            overlapCount += 1

    except EOFError:
        break

print(overlapCount)
