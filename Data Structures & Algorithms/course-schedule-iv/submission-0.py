"""
V: number of courses
E: number of edges
Q: number of queries
Time complexity: O(V + E + QVE)
Space complexity:
    - Auxiliar: O(V + E)
    - Total: O(Q + V + E)
Time: 5min
"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def isPreRequisite(source, target, visited):
            if source == target:
                return True

            if source in visited:
                return False

            visited.add(source)

            for neighbor in graph[source]:
                if isPreRequisite(neighbor, target, visited):
                    return True
            return False

        graph = {node: [] for node in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        result = []
        for u, v in queries:
            result.append(isPreRequisite(u, v, set()))
        return result
