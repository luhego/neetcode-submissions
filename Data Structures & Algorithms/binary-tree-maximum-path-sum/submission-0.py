"""
N: number of nodes in the tree
Time complexity: O(N)
Space complexity: O(N)
Time: 7min
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            local_sum = node.val + left_sum + right_sum
            self.max_path_sum = max(self.max_path_sum, local_sum)

            return node.val + max(left_sum, right_sum)

        self.max_path_sum = float("-inf")
        dfs(root)
        return self.max_path_sum