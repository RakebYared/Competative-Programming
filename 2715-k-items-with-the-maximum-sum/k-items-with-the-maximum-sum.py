class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        ans = 0

        if k:
            k, ans = k - min(k, numOnes), ans + min(k, numOnes)
        
        if k: 
            k -= min(k, numZeros)
        
        if k:
            k, ans = k - min(k, numNegOnes), ans - min(k, numNegOnes)

        return ans

        