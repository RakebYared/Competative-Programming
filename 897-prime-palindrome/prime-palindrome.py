class Solution:
    def primePalindrome(self, n: int) -> int:

        def isprime(num):
            if num == 1 or num < n:
                return False
            for x in range(2, int(num**(1/2)+1)):
                if not num % x:
                    return False
            return True

        place = int(math.log10(n))
        starter = [1,3,7,9] 

        while True:
            p = (place)//2 
            for start in starter:
                min_ = start * 10**p
                if not place:
                    for x in range(9):
                        if isprime(x):
                            return x
                else:
                    for _ in range(10**p):
                        end = 0
                        if place % 2:
                            val = min_
                        else:
                            val = min_ // 10
                        while val:
                            end *= 10
                            end += val%10
                            val //= 10
                        
                        if place % 2:
                            num = (min_ * 10**(p+1)) + end
                        else:
                            num = min_ * 10**p + (end)
                        min_ += 1

                        if isprime(num):
                            return num
            place += 1
                