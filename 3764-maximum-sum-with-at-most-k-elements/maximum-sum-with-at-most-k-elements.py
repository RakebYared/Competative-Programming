class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        cand = []

        for i,row in enumerate(grid):

            for num in nlargest(limits[i], row):
                cand.append(num)

        
        return sum(nlargest(k, cand))
        