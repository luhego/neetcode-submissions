# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time complexity: O(N)
Space complexity: O(1)
Time: 12min
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prev_left_node, left_node = None, None
        next_right_node, right_node = None, None

        pos = 1
        prev = None
        curr = head
        while curr:
            if pos == left:
                prev_left_node = prev
                left_node = curr
            elif pos == right:
                right_node = curr
                next_right_node = curr.next
    
            prev = curr
            curr = curr.next
            pos += 1

        i = (right - left)
        prev = None
        curr = left_node
        while i >= 0:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            i -= 1
        
        left_node.next = next_right_node
        if prev_left_node:
            prev_left_node.next = right_node
        
        if left_node == head:
            head = right_node
        
        return head
