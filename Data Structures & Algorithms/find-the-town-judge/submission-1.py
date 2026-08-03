"""
E: number of edges
N: number of people
Time complexity: O(E + N)
Space complexity: O(N)
Time: 7min
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = {person: 0 for person in range(1, n + 1)}
        out_degree = {person: 0 for person in range(1, n + 1)}
        for u, v in trust:
            in_degree[v] += 1
            out_degree[u] += 1

        for person, trust_count in in_degree.items():
            if trust_count == n - 1 and out_degree[person] == 0:
                return person
        
        return -1
