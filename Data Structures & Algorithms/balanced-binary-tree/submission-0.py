# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0, True

            left, left_balanced = dfs(node.left)
            right, right_balanced = dfs(node.right)

            balanced = left_balanced and right_balanced and abs(left - right) <= 1
        
            return max(left, right) + 1, balanced

        _, is_balanced = dfs(root)

        return is_balanced
