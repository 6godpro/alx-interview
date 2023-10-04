#!/usr/bin/python3
"""This module contains a function to solve
   the lockboxes challenge.
"""


def validate_boxes_is_list_of_list(boxes):
    """
       Validate the elements of boxes.
       Args:
           boxes (list): A list of lists.
       Return: True, if boxes contain lists only else False.
    """
    return all([type(box) is list for box in boxes])


def keyIsValid(key, boxes, visited):
    """A key is valid if it fits the following conditions.
       -> It is an integer.
       -> It is in this range, 0 >= key < len(boxes).
       -> It is not in the visited list.
    """
    if type(key) is int and \
            key >= 0 and \
            key < len(boxes) and \
            key not in visited:
        return True
    return False


def canUnlockAll(boxes):
    """
       Verifies that all boxes contained in boxes
       can be unlocked.
       Args:
           boxes (list): A list of lists.
       Return (boolean): True, if all boxes can be unlocked, else False
    """
    if len(boxes) == 0 or \
            not validate_boxes_is_list_of_list(boxes):
        return False

    visited = []

    def dfs(currentBox):
        visited.append(currentBox)  # stash a used key
        for key in boxes[currentBox]:  # get a new key using the current key
            if keyIsValid(key, boxes, visited):
                # explore using the new key only
                # if the key hasn't already been used
                dfs(key)
    dfs(0)  # unlock the first box
    return len(visited) == len(boxes)
