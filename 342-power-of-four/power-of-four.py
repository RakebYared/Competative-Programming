class Solution:
    def power(self, num):
        if int(num) != num or not num:
            return False

        if int(num)== 1:
            return True
        
        
        return self.power(num/4)

    def isPowerOfFour(self, n: int) -> bool:
        return self.power(n)
         



        