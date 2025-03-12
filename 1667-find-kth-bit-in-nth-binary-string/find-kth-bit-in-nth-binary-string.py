class Solution:

    def find_string(self, n):
        if n == 1:
            return '0'

        pre = self.find_string(n-1)
        rev = ['1' if b == '0' else '0' for b in pre]

        val = pre + '1' + ''.join(rev[::-1])
        
        return val



    def findKthBit(self, n: int, k: int) -> str:
        return self.find_string(n)[k-1]
        