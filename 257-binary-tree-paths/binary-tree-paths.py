# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def traverse(node, store):

            store.append(str(node.val))

            if node.left:
                traverse(node.left, store)

            if node.right:
                traverse(node.right, store)

            if not node.left and not node.right:
                ans.append('->'.join(store))

            store.pop()
        
        traverse(root, [])
        return ans
            
            

        