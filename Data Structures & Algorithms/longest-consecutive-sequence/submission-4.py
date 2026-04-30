"""
Time complexity: O(N)
Space complexity: O(N)
Time: 7min
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)

        max_seq_len = 0
        visited = set()
        for num in nums:
            # Number has been processed already
            if num in visited:
                continue
        
            seq_len = 1
            # Check backwards
            curr = num - 1
            while curr in seen:
                seq_len += 1
                curr -= 1
                visited.add(curr)

            # Check forward
            curr = num + 1
            while curr in seen:
                seq_len += 1
                curr += 1
                visited.add(curr)
            
            max_seq_len = max(max_seq_len, seq_len)
    
        return max_seq_len