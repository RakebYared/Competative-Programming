class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        nums.sort(key = lambda x : [count[x], x], reverse = True)

        ans = []
        for num in nums:
            if not ans:
                ans.append(num)

            elif ans[-1] != num:
                ans.append(num)
            
            if len(ans) == k:
                return ans
             
