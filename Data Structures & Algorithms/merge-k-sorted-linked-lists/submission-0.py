"""
N: number of lists
M: max number of elements in a list
Time complexity: O(NlogM + MNlogM) ~= O(MNlogM)
Space complexity: O(M)
Time: 11min
"""
from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for list_index, list_ in enumerate(lists):
            if list_ is None:
                continue
            heappush(min_heap, (list_.val, list_index, list_))
        
        prev = None
        head = None
        while min_heap:
            val, list_index, list_ = heappop(min_heap)

            curr = ListNode(val)
            if head is None:
                head = curr
            if prev is not None:
                prev.next = curr
            prev = curr

            if list_.next:
                list_ = list_.next
                heappush(min_heap, (list_.val, list_index, list_))
        
        return head
