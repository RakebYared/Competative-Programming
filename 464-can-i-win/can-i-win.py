class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        dp = {}

        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        
        def play (nums, total):

            key = (tuple(sorted(nums)), total)
            if key in dp:
                return dp[key]   
                
            if max(nums) >= total:
                dp[key] = True
                return True
            item = list(nums)

            for num in item:
                temp = set(nums)
                temp.remove(num)
                if not play(temp, total-num):
                    dp[key] = True
                    return True
            dp[key] = False
            return False        
        
        return play(set([x for x in range(1,maxChoosableInteger+1)]),desiredTotal)
    