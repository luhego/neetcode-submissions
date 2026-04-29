"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = defaultdict(Node)
        copy_to_original = defaultdict(Node)

        new_head = None
        previous = None
        current = head
        while current:
            node = Node(current.val)

            original_to_copy[current] = node
            copy_to_original[node] = current

            if new_head is None:
                new_head = node

            if previous:
                previous.next = node
            previous = node

            current = current.next

        current = new_head
        while current:
            original = copy_to_original[current]
            original_random = original.random

            if original_random is not None:
                copy_random = original_to_copy[original_random]
                current.random = copy_random

            current = current.next

        return new_head
