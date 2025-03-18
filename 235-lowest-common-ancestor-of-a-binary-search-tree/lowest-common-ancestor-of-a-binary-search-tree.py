# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(node):
            if node.val < q.val and node.val < p.val:
                return search(node.right)
            elif node.val > q.val and node.val > p.val:
                return search(node.left)
            else:
                return node
        
        return search(root)

        