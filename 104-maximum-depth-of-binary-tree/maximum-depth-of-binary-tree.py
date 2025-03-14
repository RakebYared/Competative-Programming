# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:

        if node:
            right = 1 + self.maxDepth(node.right)
            left = 1 + self.maxDepth(node.left)

            return max(right, left)

        return 0
    #
        