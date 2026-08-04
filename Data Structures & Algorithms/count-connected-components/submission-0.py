"""
Time complexity: O(V + E)
Space complexity: O(V + E)
Time: 3min
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        graph = {node: [] for node in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        components = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            components += 1

        return components   