class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if not n:
            return 0

        value = self.fib(n-1) + self.fib(n-2)
        return value
        