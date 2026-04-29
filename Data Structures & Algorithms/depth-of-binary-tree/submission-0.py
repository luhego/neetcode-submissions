# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverseTree(node, level=0):
            if node is None:
                return

            if node.left is None and node.right is None:
                self.global_max_depth = max(self.global_max_depth, level)
        
            traverseTree(node.left, level + 1)
            traverseTree(node.right, level + 1)

        self.global_max_depth = 0
        traverseTree(root, 1)
        return self.global_max_depth 
