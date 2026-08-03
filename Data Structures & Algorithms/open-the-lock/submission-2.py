"""
Time complexity: O(10^4) = O(1)
Space complexity: O(10^4) = O(1)
Time: 15min
Approach:
For each node, generate all next states. E.g.: 0000 -> 1000, 9000, 0100, 0900, 0010, 0090, 0001, 0009
Use BFS to find the minimum total number of turns
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNextStates(node):
            states = []
            for i in range(4):
                digit = int(node[i])
                up = str((digit + 1) % 10)
                states.append(node[:i] + up + node[i+1:])

                down = str((digit - 1) % 10)
                states.append(node[:i] + down + node[i+1:])
            return states

        source = "0000"
        deadends_set = set(deadends)
        if source in deadends_set:
            return -1

        queue = deque([(source, 0)])
        visited = set([source])
        while queue:
            node, turns = queue.popleft()

            if node == target:
                return turns

            for next_node in getNextStates(node):
                if next_node in deadends_set:
                    continue
                if next_node in visited:
                    continue
                
                visited.add(next_node)
                queue.append((next_node, turns + 1))
        
        return -1

