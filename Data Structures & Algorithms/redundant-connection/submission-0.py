"""
Time complexity: O(V + E + E*(E + V)) = O(E(E+V))
Space complexity: O(V + E)
Time: 15min
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def removeEdge(u, v):
            graph[u].remove(v)
            graph[v].remove(u)
        
        def addEdge(u, v):
            graph[u].add(v)
            graph[v].add(u)

        def isValid():
            visited = set([1])
            queue = deque([(1, None)])
            while queue:
                node, parent = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        return False
                    visited.add(neighbor)
                    queue.append((neighbor, node))
            
            return len(visited) == n

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        n = len(graph)

        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            removeEdge(edge[0], edge[1])
            if isValid():
                return edge
            addEdge(edge[0], edge[1])

        return []
