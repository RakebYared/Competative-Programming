class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        store = defaultdict(int)
        store[0]=1 
        ps = 0
        for i in range(len(nums)):
            ps += nums[i]
            count += store[ps-k] or 0
            store[ps]+=1
        return count