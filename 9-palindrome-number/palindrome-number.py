class Solution:
    def isPalindrome(self, x: int) -> bool:
        num, y = x, 0
        if num == 0:
            return True
        n = int(math.log10(abs(num)))
        while num>0:
            y+= 10**n * (num%10)
            num //= 10
            n -= 1
        return x == y