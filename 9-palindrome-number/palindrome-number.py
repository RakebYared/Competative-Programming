class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        n = len(y)
        for i in range(len(y)//2):
            if y[i] != y[n-i-1]:
                return False
        return True
    