class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []


        def compute(val, store):
            if len(val) == n:
                ans.append(val.copy())
            
            nums = store.copy()

            for num in nums:
                store.remove(num)
                val.append(num)
                compute(val, store)
                store.add(num)
                val.pop()
            
        compute([], set(nums))
        return ans


        