class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        count = 1

        if k == 1:
            ans.append(nums[0])

        for i in range(1,n):
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                count = 1
            
            if i+1 >= k:
                if count >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)

        return ans
            

