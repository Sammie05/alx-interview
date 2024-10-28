#!/usr/bin/python3

""" a method that can determines if all boxes can be opened """


def canUnlockAll(Boxes):
    """ a method that determines if all boxes are opened """
    unlocked = {0}
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unclocked.add(key)
                stack.append(key)

    return len(unlocked) == len(boxes)
