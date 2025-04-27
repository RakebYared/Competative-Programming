# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        
        if not root:
            return []

        ans = []

        def traverse(node,store):

            store.append(node.val)

            if node.left:
                traverse(node.left, store)
            
            if node.right:
                traverse(node.right, store)
            
            if not node.left and not node.right:
                if sum(store) == targetSum:
                    ans.append(store.copy())
            
            store.pop()

        traverse(root, [])

        return ans

        