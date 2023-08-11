def canUnlockAll(boxes):
    if len(boxes) == 0:
        return

    for i in range(len(boxes)):
        box = boxes[i]#the new box marked with key/new key
        #find a way to start with the first key and then update with the new key
        #recursion should be called with the new ox pointed

        for key in box:
            #delete the key in this box update list/boxes
            if "open" not in boxes[key]:
                boxes[key].append("open")

    print(boxes)

canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])


