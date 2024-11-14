class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod = {0:-1}
        add = 0
        for i in  range(len(nums)):
            add+=nums[i]
            if add%k in mod:
                if i - mod[add%k] >1:
                    return True
            else:
                mod[add%k] = i
        return False