class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_coins = 0
        piles.sort()
        for coin in piles[(len(piles)//3)::2]:
            max_coins += coin
        return max_coins
        
        