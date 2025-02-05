class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: float('infinity') if x<0 else -float('infinity'))
        ans = []
        mid = len(nums)//2
        for i in range(mid):
            ans.append(nums[i])
            ans.append(nums[i+mid])
        return ans        