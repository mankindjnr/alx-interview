#!/usr/bin/python3
"""
method that determines if all the boxes can be opened.
Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
"""


def canUnlockAll(boxes):
    """a method that opens all boxes
    """
    for j in range(len(boxes)):
        if "removed" not in boxes[0] and "open" not in boxes[0]:
            boxes[0].append("open")

        for item in boxes:
            if "open" in item and "removed" not in item:
                opened = item[:-1]
                break

        for i in range(len(boxes)):
            if i in opened:
                if "open" not in boxes[i]:
                    boxes[i].append("open")

        for item in boxes:
            if opened == item[:-1]:
                item.append("removed")

    for item in boxes:
        if "open" not in item:
            return False

    return True
