class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequencies = set()

        for num in nums:
            if num in frequencies:
                return True
            frequencies.add(num)
        
        return False
         