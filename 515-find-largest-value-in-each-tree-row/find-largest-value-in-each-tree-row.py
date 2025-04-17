# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        store = defaultdict(lambda : -float('inf'))

        def traverse(node, level):

            if node:
                store[level] = max(node.val, store[level])
                traverse(node.right, level + 1)
                traverse(node.left, level + 1)
        
        traverse(root, 0)
        return list(store.values())

            