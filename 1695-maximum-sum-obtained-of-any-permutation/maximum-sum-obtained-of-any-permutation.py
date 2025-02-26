class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        ps = [0]*(n+1)

        for start, end in requests:
            ps[start] += 1
            ps[end+1] -= 1
        
        for i in range(1,n):
            ps[i] += ps[i-1]
        
        ps.sort(reverse = True)
        nums.sort(reverse = True)
        

        ans = 0
        for i in range(n):
            ans += ps[i] * nums[i]
        
        return ans % (10**9 + 7)

        