"""
Approach:

Add all numbers to a set or dict. Extract any number from the set and look backwards and forwards.

Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)


        lon_seq_len = 0
        while seen:
            curr_seq_len = 1
            curr_num = seen.pop()

            next_num = curr_num + 1
            # Move forward
            while next_num in seen:
                curr_seq_len += 1
                seen.remove(next_num)
                next_num += 1


            prev_num = curr_num - 1
            # Move backward
            while prev_num in seen:
                curr_seq_len += 1
                seen.remove(prev_num)
                prev_num -= 1

            lon_seq_len = max(lon_seq_len, curr_seq_len)

        return lon_seq_len