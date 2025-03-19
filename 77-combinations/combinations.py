class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def compute(val, num):
            if len(val) == k:
                ans.append(val.copy())
                return

            for num in range(num, n+1):
                val.append(num)
                compute(val, num+1)
                val.pop()
        
        compute([], 1)
        return ans
        