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
    if boxes == [] or \
            not validate_boxes_is_list_of_list(boxes):
        return False

    visited = [0]
    queue = Queue()
    queue.enqueue(0)

    while queue.length != 0:  # run until queue is empty
        currentBox = queue.dequeue()  # retrieve the next key

        if currentBox is None:
            break

        for key in boxes[currentBox]:
            if keyIsValid(key, boxes, visited):
                visited.append(key)
                queue.enqueue(key)
    return len(visited) == len(boxes)


class Node:
    """A class representing a Node."""
    def __init__(self, value, node=None):
        self.value = value
        self.next_node = node


class Queue:
    """A class representing a Queue data structure."""
    def __init__(self):
        self.head = None
        self.__count = 0

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            node.next_node = None
            self.head = node
        else:
            tmp = self.head
            while tmp.next_node:
                tmp = tmp.next_node
            tmp.next_node = node
            node.next_node = None
        self.__count += 1

    def dequeue(self, index=0):
        node = self.head
        self.head = node.next_node if node else None
        self.__count -= 1
        return node.value if node else None

    @property
    def length(self):
        return self.__count
