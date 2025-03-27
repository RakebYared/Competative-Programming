# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        def search_left(node):
            if node:
                left.append(node.val)
                search_left(node.left)
                search_left(node.right)
            else:
                left.append(node)
                
        def search_right(node):
            if node:
                right.append(node.val)
                search_right(node.right)
                search_right(node.left)
            else:
                right.append(node)
        
        search_right(root)
        search_left(root)

        print(right, left)

        return right == left