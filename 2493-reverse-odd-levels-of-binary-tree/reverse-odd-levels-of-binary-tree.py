# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverse(node1, node2, flag):

            if not node1:
                return

            if flag:
                node1.val,  node2.val = node2.val, node1.val

            reverse(node2.right, node1.left, not flag)
            reverse(node1.right, node2.left, not flag)

        reverse(root.left, root.right, True)
        return root

        