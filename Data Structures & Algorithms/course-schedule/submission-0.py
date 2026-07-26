"""
V: number of nodes
E: number of edges
Time complexity: O(V + E)
Space complexity: O(V)
Time: 8min
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        sources = deque([])
        for node, degree in in_degree.items():
            if degree == 0:
                sources.append(node)

        taken_courses = 0
        while sources:
            node = sources.popleft()
            taken_courses += 1

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    sources.append(neighbor)
            
        return taken_courses == numCourses
