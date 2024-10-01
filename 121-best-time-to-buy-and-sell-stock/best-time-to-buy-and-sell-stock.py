class Solution:
    def maxProfit(self, price: List[int]) -> int:
        res = 0
        if len(price)==1:
            return res
        for i in range(1,len(price)):
            if price[i]>price[i-1]:
                res = max(res, price[i]-price[i-1])
                price[i]=price[i-1]
        return res
        
        
        
        
        
        
