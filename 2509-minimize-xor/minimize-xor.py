class Solution:
    def count_ones(self, num):
        count = 0
        for bit in range(30):
            if (num >> bit) & 1 :
                count += 1
        return count 


    def minimizeXor(self, num1: int, num2: int) -> int:

        ones1, ones2 = self.count_ones(num1), self.count_ones(num2)

        if ones1 == ones2:
            return num1

        elif ones1 > ones2:

            x = 0
            bit = 29
            count = ones2 

            while count :
                if num1 >> bit & 1:
                    x |= (1 << bit)
                    count -= 1
                bit -= 1
        
        else:
            x = num1
            bit = 0
            count = ones2 - ones1

            while count :
                if not (num1 >> bit & 1):
                    x |= (1 << bit)
                    count -= 1
                bit += 1
           
        return x




        