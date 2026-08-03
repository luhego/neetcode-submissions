"""
N: number of nodes
E: number of edges
Time complexity: O(N + E)
Space complexity: O(N)
Time: 9min
Approach:
Perform BFS passing the current node and its parent. If a neighbor
is marked as visited but it is not the current parent, we have detected a cycle.
Verify that the number of visited nodes matches the total number of nodes(no islands).
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set([0])
        queue = deque([(0, None)])
        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if neighbor in visited:
                    # Cycle detected
                    if neighbor != parent:
                        return False
                    continue

                visited.add(neighbor)
                queue.append((neighbor, node))
        
        return len(visited) == n
