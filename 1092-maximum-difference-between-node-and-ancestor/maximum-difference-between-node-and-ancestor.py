# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxx = -1
        minn = float('inf')
        ans = -1

        def search(node):
            nonlocal maxx, minn, ans

            if node:
                maxx = max(maxx, node.val)
                minn = min(minn, node.val)
                temp = [minn,maxx]
                ans = max(ans, maxx-minn)

                search(node.right)
                minn,maxx = temp
                search(node.left)
                minn,maxx = temp
        
        search(root)
        return ans
            
        

            
            