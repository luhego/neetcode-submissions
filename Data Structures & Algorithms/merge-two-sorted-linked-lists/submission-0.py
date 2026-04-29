# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        previous = None
        current = None
    
        while list1 or list2:
            if not list1:
                current = list2
                list2 = list2.next
            elif not list2:
                current = list1
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    current = list1
                    list1 = list1.next
                else:
                    current = list2
                    list2 = list2.next

            if  not head:
                head = current

            if previous:
                previous.next = current

            previous = current

        return head
