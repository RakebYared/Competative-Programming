class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def compute(val, num):
            if len(val) == k:
                ans.append(val)
                return

            for num in range(num, n+1):
                compute(val+[num], num+1)
        
        compute([], 1)
        return ans
        