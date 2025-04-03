# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def traverse(node):
            nonlocal ans

            if not node:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            best = max(node.val + right, node.val+left, node.val)
            ans = max(ans, left + right + node.val, best)
             

            return best

        traverse(root)
        return ans