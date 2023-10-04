#!/usr/bin/python3
"""This module containts a function to solve
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


def canUnlockAll(boxes):
    """
       Verifies that all boxes contained in boxes
       can be unlocked.
       Args:
           boxes (list): A list of lists.
       Return: True, if boxes contain lists only else False.
    """
    if not validate_boxes_is_list_of_list(boxes):
        return False

    visited = []

    def dfs(currentBox):
        visited.append(currentBox)
        for key in boxes[currentBox]:
            if key not in visited and key < len(boxes):
                dfs(key)
    dfs(0)
    return len(visited) == len(boxes)
