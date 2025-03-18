#         self.right = right
#         self.right = right
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return 
        
        if node.val > key:
            node.left = self.deleteNode(node.left, key)
        elif node.val < key:
            node.right = self.deleteNode(node.right, key)

        elif node.val == key:
            temp = node.right
            if temp:
                while temp.left:
                    temp = temp.left                
                node.val = temp.val
                node.right = self.deleteNode(node.right, node.val)
                
            else:
                return node.left
        
        return node
        

        