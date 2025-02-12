class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0
        i = 0
        swaps = 0

        while i < n and swaps <= n:
            temp = nums[i]
            j = (i + k) % n

            while j != start and swaps < n:
                j = (i + k) % n
                nums[j], temp = temp, nums[j]
                i = j 
                swaps += 1
            
            start += 1
            i = start

            # nums[j] = temp


