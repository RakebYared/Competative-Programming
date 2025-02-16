class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        num = abs(x)

        while num:
            new_num *= 10
            new_num += (num % 10)
            num //= 10
        
        if new_num >= 2147483648:
            return 0
        elif x < 0 :
            return -1 * new_num
        else:
            return new_num


