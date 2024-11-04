
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def tonumber(num):
            n = 0
            ten = 1
            while num:
                n += int(num[-1]) * ten
                ten*=10
                num = num[:-1]
            return n
        return str(tonumber(num1) * tonumber(num2))
