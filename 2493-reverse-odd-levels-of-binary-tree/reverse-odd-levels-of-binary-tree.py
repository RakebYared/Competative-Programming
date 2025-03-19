# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        store = deque()

        def moveright(node, toggle):
            nonlocal store

            if node:
                if toggle:
                    store.append(node.val)
                moveright(node.right, not toggle)
                moveright(node.left, not toggle )
            
        def moveleft(node, toggle):
            if node:
                if toggle:
                    node.val = store.popleft()
                moveleft(node.left, not toggle)
                moveleft(node.right, not toggle)

        moveright(root, False)
        moveleft(root, False)

        return root
        