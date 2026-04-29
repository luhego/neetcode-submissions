# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def findMiddleNode(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse(head):
            previous = None
            current = head
            while current:
                next_ = current.next
                current.next = previous
                previous = current
                current = next_

            return previous

        mid_node = findMiddleNode(head)
        last = reverse(mid_node)

        new_head = None
        p1 = head
        p2 = last
        previous = None
        while p1 and p2:
            temp_p1 = p1.next
            temp_p2 = p2.next

            if not new_head:
                new_head = p1

            if previous:
                previous.next = p1
            previous = p2

            p1.next = p2
            p2.next = None

            p1 = temp_p1
            p2 = temp_p2
