class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)

        max_len = 0
        for num in nums:
            if num - 1 in seen:
                continue

            count = 1
            while num + 1 in seen:
                num += 1
                count += 1
            
            max_len = max(max_len, count)
    
        return max_len
