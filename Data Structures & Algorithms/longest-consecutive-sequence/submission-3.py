class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited = set()

        max_len = 0
        for num in nums:
            if num in visited:
                continue

            curr_len = 1
            prev_num = num - 1
            while prev_num in nums_set:
                visited.add(prev_num)
                curr_len += 1
                prev_num -= 1

            next_num = num + 1
            while next_num in nums_set:
                visited.add(prev_num)
                curr_len += 1
                next_num += 1

            max_len = max(max_len, curr_len)
        
        return max_len