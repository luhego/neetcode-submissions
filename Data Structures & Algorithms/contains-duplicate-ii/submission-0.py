class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        visited = defaultdict(int)
        for i in range(n):
            if nums[i] in visited:
                if abs(i - visited[nums[i]]) <= k:
                    return True
            visited[nums[i]] = i

        return False
        