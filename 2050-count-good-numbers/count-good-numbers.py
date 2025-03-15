class Solution:
    def countGoodNumbers(self, n: int) -> int:
        dp = {}
        mod = 10**9 + 7

        def power(n, x):
            if (n, x) in dp:
                return dp[(n, x)] 
            if x == 0:
                return 1
            if x == 1:
                return n  
            
            half = power(n, x // 2) % mod  
            if x % 2 == 1:
                value = (n * half * half) % mod  
            else:
                value = (half * half) % mod 

            dp[(n, x)] = value  
            return value

        even_count = (n + 1) // 2
        odd_count = n // 2  

        even_part = power(5, even_count) % mod
        odd_part = power(4, odd_count) % mod

        return (even_part * odd_part) % mod