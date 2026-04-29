class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        visited = set()
        for num in nums:
            nums_set.add(num)

        max_length = 0
        for num in nums:
            if num in visited:
                continue
            visited.add(num)

            curr_length = 1
            left = num - 1
            while left in nums_set:
                curr_length += 1
                left -= 1
            
            right = num + 1
            while right in nums_set:
                curr_length += 1
                right += 1

            max_length = max(max_length, curr_length)

        return max_length