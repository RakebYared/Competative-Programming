# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        ans = []

        def traverse(node, store):

            store.append(chr(node.val + 97))

            if node.right:
                traverse(node.right, store)
            
            if node.left:
                traverse(node.left, store)
            
            if not node.left and not node.right:
                ans.append(''.join(store[::-1]))
            
            store.pop()

        traverse(root, [])
        return min(ans)
        