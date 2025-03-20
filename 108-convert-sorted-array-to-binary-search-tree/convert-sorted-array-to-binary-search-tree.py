# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def backtrack(nums):
            if not len(nums):
                return None

            mid = len(nums)//2
        
            left = backtrack(nums[:mid])
            right = backtrack(nums[mid+1:])

            node = TreeNode(nums[mid], left, right)

            return node
        
        return backtrack(nums)
        