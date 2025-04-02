class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        i = 0
        n = len(nums)
        ans = []

        while i < n:

            if nums[i] != i + 1:
                new_ind = nums[i] - 1

                if nums[new_ind] == nums[i]:
                    i += 1
                else:
                    nums[i], nums[new_ind] = nums[new_ind], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])
        
        return ans