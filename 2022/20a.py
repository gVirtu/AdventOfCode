from __future__ import annotations


class List:
    zero: Node | None
    length: int

    def __init__(self, zero):
        self.zero = zero
        self.length = 1

    def print(self):
        current = self.zero

        while True:
            assert isinstance(current, Node)
            print(current.value, end=" ")
            current = current.next

            if current == self.zero:
                print()
                break


class Node:
    value: int
    next: Node | None
    prev: Node | None
    origNext: Node | None

    def __init__(self, value, prev: Node | None):
        self.value = value
        self.prev = prev
        if prev:
            prev.next = self
            prev.origNext = self
        self.origNext = None
        self.next = None

    def jump(self, direction):
        return {"next": self.next, "prev": self.prev}[direction]


lastNode = None
firstNode = None
linkedList = None
listLength = 0

while True:
    try:
        nodeValue = int(input())
        currentNode = Node(nodeValue, lastNode)

        if firstNode is None:
            firstNode = currentNode

        if nodeValue == 0:
            linkedList = List(currentNode)

        lastNode = currentNode
        listLength += 1

    except EOFError:
        break

assert isinstance(firstNode, Node)
assert isinstance(lastNode, Node)
assert isinstance(linkedList, List)

firstNode.prev = lastNode
lastNode.next = firstNode
linkedList.length = listLength

currentNode = firstNode

while currentNode is not None:
    if currentNode.value == 0:
        currentNode = currentNode.origNext
        continue

    # Must mod by len-1 because of circular list
    # e.g. 2 3 1 when processing 2 gives 3 1 2 which is essentially the same list

    shiftAmount = abs(currentNode.value) % (listLength - 1)
    shiftPointer = "next" if currentNode.value >= 0 else "prev"

    shiftNode = currentNode
    # print(
    #     f"Starting at {currentNode.value} should jump {shiftAmount} {shiftPointer}: ",
    #     end="",
    # )
    while shiftAmount > 0:
        assert isinstance(shiftNode, Node)
        shiftNode = shiftNode.jump(shiftPointer)
        assert isinstance(shiftNode, Node)
        # print(shiftNode.value)
        shiftAmount -= 1
    # print("")

    assert isinstance(shiftNode, Node)
    assert isinstance(shiftNode.prev, Node)
    assert isinstance(shiftNode.next, Node)
    assert isinstance(currentNode, Node)
    assert isinstance(currentNode.prev, Node)
    assert isinstance(currentNode.next, Node)

    # Remove currentNode from its position, rewiring neighbors
    currentNode.prev.next = currentNode.next
    currentNode.next.prev = currentNode.prev

    # Insert currentNode right after (or before) shiftNode
    if shiftPointer == "next":
        shiftNodeFormerNext = shiftNode.next
        shiftNode.next = currentNode
        currentNode.prev = shiftNode

        currentNode.next = shiftNodeFormerNext
        shiftNodeFormerNext.prev = currentNode
    else:
        shiftNodeFormerPrev = shiftNode.prev
        shiftNode.prev = currentNode
        currentNode.next = shiftNode

        currentNode.prev = shiftNodeFormerPrev
        shiftNodeFormerPrev.next = currentNode

    # linkedList.print()

    currentNode = currentNode.origNext

linkedList.print()

groveCoordinates = 0
currentNode = linkedList.zero
currentIndex = 0

while currentIndex < 3000:
    assert isinstance(currentNode, Node)
    currentNode = currentNode.next
    currentIndex += 1

    if currentIndex % 1000 == 0:
        assert isinstance(currentNode, Node)
        groveCoordinates += currentNode.value

print(groveCoordinates)
