# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left + right > self.max_global_diameter:
                self.max_global_diameter = left + right

            return max(left, right) + 1

        self.max_global_diameter = 0
        dfs(root)

        return self.max_global_diameter
