"""
Time complexity: O(N)
Space complexity: O(N) including answer otherwise O(k)
Time: 32min
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = []
        queue = deque([])
        left = 0
        for right in range(n):
            while len(queue) > 0 and queue[-1][1] <= nums[right]:
                queue.pop()
            queue.append((right, nums[right]))

            if right - left + 1 == k:
                answer.append(queue[0][1])
                left += 1

            if queue[0][0] <= right - k + 1:
                queue.popleft()
        
        return answer