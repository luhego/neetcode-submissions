# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Reverse it
        n = len(nodes)
        head = nodes[-1]
        for i in range(n - 2, -1, -1):
            nodes[i + 1].next = nodes[i]
        
        nodes[0].next = None

        return head
