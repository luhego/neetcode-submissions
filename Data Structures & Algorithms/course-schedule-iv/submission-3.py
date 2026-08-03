"""
Solution A: Naive solution using dfs for each query
V: number of courses
E: number of edges
Q: number of queries
Time complexity: O(V + E + Q(V + E)) = O(Q(V + E))
Space complexity:
    - Auxiliar: O(V + E)
    - Total: O(Q + V + E)
Time: 5min

Solution B: Pre-compute prerequisites
Time complexity: O(V + E + V(V + E) + Q) = O(V(V + E) + Q)
Space complexity: O(V) -> auxiliar, total: O(V + Q)
Time: 20min
"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(node):
            if all_prerequisites[node]:
                return {node}.union(all_prerequisites[node])

            reachable = set()
            for neighbor in graph[node]:
                reachable = reachable.union(dfs(neighbor))

            all_prerequisites[node] = reachable.copy()

            reachable.add(node)
            return reachable      

        # Build graph
        graph = {node: [] for node in range(numCourses)}
        in_degre = {node: 0 for node in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
            in_degre[b] += 1

        # Pre-compute prerequisites
        all_prerequisites = {node: set() for node in range(numCourses)}
        for node, degree in in_degre.items():
            if degree != 0:
                continue
            if all_prerequisites[node]:
                continue
            dfs(node)
        
        result = []
        for u, v in queries:
            result.append(v in all_prerequisites[u])
        return result

