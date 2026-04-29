from heapq import heappush, heappop
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(arr, left, right):
            pivot_index = random.randint(left, right)
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

            pivot = arr[right]
            p = left
            for i in range(left, right):
                if freqs[arr[i]] <= freqs[pivot]:
                    arr[i], arr[p] = arr[p], arr[i]
                    p += 1
            
            arr[p], arr[right] = arr[right], arr[p]
    
            return p

        def quickSelect(arr, left, right):
            if left == right:
                return left
            partition_index = partition(arr, left, right)

            if k > partition_index:
                return quickSelect(arr, partition_index + 1, right)
            elif k < partition_index:
                return quickSelect(arr, left, partition_index - 1)
            else:
                return k


        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        keys = list(freqs.keys())
        if len(freqs) <= k:
            return keys

        k = len(keys) - k
        quickSelect(keys, 0, len(keys) - 1)

        return keys[k:]
