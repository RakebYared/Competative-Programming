class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == float(1):
            return True

        if n == 0:
            return False

        if n % 4:
            return False
        
        return self.isPowerOfFour(n/4)
        