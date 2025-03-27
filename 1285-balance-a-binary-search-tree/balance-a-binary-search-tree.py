# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []

        def search(node):
            if node:
                search(node.left)
                nums.append(node.val)
                search(node.right)

        search(root)
        
        def divide(nums):
            if nums:
                mid = len(nums)//2

                right = divide(nums[mid+1:])
                left = divide(nums[:mid])

                return TreeNode(nums[mid], left, right)
        
        return divide(nums)
        