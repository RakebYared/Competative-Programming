class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less_nums = 0
        equal_nums = 0

        for num in nums:
            if num < target:
                less_nums += 1
            elif num == target:
                equal_nums += 1

        if equal_nums:
            return [target_index for target_index in range(less_nums, less_nums + equal_nums)]
        
        else:
            return []


        
        