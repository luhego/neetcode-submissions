# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
N: size of list1
M: size of list2
TC: O(N + M)
SC: O(1) without counting auxiliar space for the solution
Time: 5min
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        curr = None

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    curr = list1
                    list1 = list1.next
                else:
                    curr = list2
                    list2 = list2.next
            elif list1:
                curr = list1
                list1 = list1.next
            elif list2:
                curr = list2
                list2 = list2.next

            if prev:
                prev.next = curr
            
            prev = curr


            if not head:
                head = curr
        
        return head
