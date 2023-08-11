boxes =[[1], [2], [3], [4], [5]] # true
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # true
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]] # false
from pprint import pprint

def unlock(boxes):
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

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(unlock(boxes))