"""
 Insert Node at the beginning of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Insert(head, data):
    new_Node = Node(data)
    new_Node.next = head
    head = new_Node
    return head
