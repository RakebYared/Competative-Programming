class Solution:
    def factorial(num):
        if num == 1 or num == 0:
            return 1

        return num * factorial(num)

    def trailingZeroes(self, n: int) -> int:
        x = factorial(n)

        count = 0
        while x:
            if x % 10:
                break
            count += 1
            x //= 10
        
        return count

        