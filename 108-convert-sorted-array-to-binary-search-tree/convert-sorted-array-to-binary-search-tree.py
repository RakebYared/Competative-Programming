# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            mid = len(nums) // 2

            right = self.sortedArrayToBST(nums[mid+1:])
            left = self.sortedArrayToBST(nums[:mid])
            
            return TreeNode(nums[mid], left, right)

