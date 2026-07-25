# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time complexity: O(N)
Space complexity: O(1)
Time: 15min
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if node is None:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            local_diameter = left + right
            self.global_diameter = max(self.global_diameter, local_diameter)

            return max(left, right) + 1

        self.global_diameter = 0
        traverse(root)
        return self.global_diameter
        