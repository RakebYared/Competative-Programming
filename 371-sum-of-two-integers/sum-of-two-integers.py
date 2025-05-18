class Solution:
    def getSum(self, num1: int, num2: int) -> int:

        num1 &= 4095
        num2 &= 4095

        def bitAdder(a,b,c):
            val = a ^ b ^ c
            c = a & b | a & c | b & c

            return val, c

        c = 0
        ans = 0

        for bit in range(12):

            a = (num1 >> bit) & 1
            b = (num2 >> bit) & 1

            val, c = bitAdder(a,b,c)

            ans |= (val << bit)
            bit += 1 
        
        if (ans >> 11) & 1:
            ans -= 4096 

        return ans
        

































