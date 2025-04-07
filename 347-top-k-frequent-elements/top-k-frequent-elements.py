class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        nums = sorted(count.keys(), key = lambda x : count[x], reverse = True)
        ans = []

        for num in nums:
            if not k:
                break
            ans.append(num)
            k -= 1
        
        return ans


        
             
