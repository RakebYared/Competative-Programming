# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def search(node, maxx, minn):
            if node:
                right = search(node.right, max(maxx, node.val), min(minn, node.val))
                left = search(node.left, max(maxx, node.val), min(minn, node.val))
            
            
                return max(right, left)
            return maxx - minn
        
        return search(root, root.val, root.val)



            
            