# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def traverse(tree_node, list_node):

            if not list_node:
                return True
            
            if not tree_node:
                return False
            
            if tree_node.val != list_node.val:
                return False
            
            left = traverse(tree_node.left, list_node.next)
            right = traverse(tree_node.right, list_node.next)

            if left or right:
                return True
            
            return False
        

        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == head.val and traverse(node, head):
                return True


            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            

        return False