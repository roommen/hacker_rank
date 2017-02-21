"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    visited = {}
    while head:
        if head in visited:
            return True
        else:
            visited[head] = 1
        head = head.next
    return False
