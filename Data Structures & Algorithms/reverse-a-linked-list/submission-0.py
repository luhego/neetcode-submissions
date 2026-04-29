# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        
        current = head
        while current:
            nodes.append(current)
            current = current.next

        new_head = None
        previous = None
        for node in nodes[::-1]:
            if new_head is None:
                new_head = node
            else:
                previous.next = node
            
            previous = node
            node.next = None

        return new_head