"""
Time complexity: O(9^4) = O(1)
Space complexity: O(9^4) = O(1)
Time: 15min
Approach:
For each node, generate all next states. E.g.: 0000 -> 1000, 9000, 0100, 0900, 0010, 0090, 0001, 0009
Use BFS to find the minimum total number of turns
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNextStates(node):
            node_list = [int(char) for char in node]
            states = []
            for i in range(4):
                prev = node_list[i]
                node_list[i] = (node_list[i] - 1 if node_list[i] > 0 else 9)
                states.append("".join(str(val) for val in node_list))
                node_list[i] = prev
        
                prev = node_list[i]
                node_list[i] = (node_list[i] + 1 if node_list[i] < 9 else 0)
                states.append("".join(str(val) for val in node_list))
                node_list[i] = prev
        
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

