# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def summer(node, num):
            nonlocal ans
            if node:
                if not node.left and not node.right:
                    ans += ((num*10) + node.val) 
                if node.right:
                    summer(node.right, (num*10) + node.val)
                
                if node.left:
                    summer(node.left, (num*10) + node.val)

        summer(root, 0)
        return ans 
            