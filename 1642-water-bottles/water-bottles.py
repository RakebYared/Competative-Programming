class Solution:
    def numWaterBottles(self, num: int, ex: int) -> int:
        res = num
        while num>=ex:
            rem = num%ex  
            num//= ex   
            res+=num   
            num+=rem   

        return res

        