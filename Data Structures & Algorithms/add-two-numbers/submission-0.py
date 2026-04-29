# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        new_head = None
        previous = None
        current = None
        carry = 0
        while p1 or p2:
            sum_ = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            carry = sum_ // 10
            sum_ = sum_ % 10

            current = ListNode(sum_)
            if not new_head:
                new_head = current
    
            if previous:
                previous.next = current

            previous = current

            p1 = p1.next if p1 else p1
            p2 = p2.next if p2 else p2

        if carry > 0:
            current.next = ListNode(carry)

        return new_head