"""
Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = min(heights[left], heights[right]) * (right - left)

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
        
        return max_area
        