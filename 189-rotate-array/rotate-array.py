class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        moved = k % n

        ans = nums[n-moved: n] + nums[0 : n - moved]
        for i in range(n):
            nums[i] = ans[i]
