# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time complexity: O(N)
Space complexity: O(H)
Time: 3min
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        left_to_right = True
        queue = deque([root])
        levels = []
        while queue:
            level = []
            queue_size = len(queue)
            for _ in range(queue_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if left_to_right:
                levels.append(level)
            else:
                levels.append(level[::-1])
            
            left_to_right = not left_to_right
        
        return levels
