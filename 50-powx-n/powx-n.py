class Solution:

    def myPow(self, x: float, n: int) -> float:

        def compute(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            half = compute(x, n//2)

            return x * half * half if n % 2 else half * half

        if n < 0:
            return 1 / compute(x, abs(n))
        else:
            return compute(x, n)



        