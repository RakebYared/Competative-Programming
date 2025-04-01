class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        nums = []
        for row in matrix:
            nums += row
        
        i = bisect_left(nums,target)

        return nums[i%len(nums)] == target
        

        return False

        