# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1

        # Delete the first node
        if fast is None:
            current = head
            current = current.next
            head.next = None
            return current

        while fast.next:
            slow = slow.next
            fast = fast.next

        to_delete = slow.next
        slow.next = to_delete.next
        to_delete.next = None

        return head