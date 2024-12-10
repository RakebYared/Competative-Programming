class Solution:
    def judgeSquareSum(self, c: int) -> bool:
# 0 1 3.......-2 -1 sqrt(c) o(n): 
        l, r = 0, int(sqrt(c))
        while l<=r:
            m = (l+r)//2
            rem = sqrt(c - (m*m))
            if rem == int(rem):
                return True
            l+=1
        return False
'''
8^ + 6^ =100
0  .....  10 
m 5 : rem = 100-25 = 75 = 8.66 but its not int but since its > than m l=m+1
m 8 : rem = 100-64 = 36 = 6 since 6 is int and < 10 

0 ... 7
m 3: rem = 50-9=41 = 6.4  l=m+1 bc rem > m
m 5: rem = 5 

0...4
m = 2, rem = 16-4=12= 3.4 rem>m
m = 3, rem = 16-9= 7 = 2.6 

'''

