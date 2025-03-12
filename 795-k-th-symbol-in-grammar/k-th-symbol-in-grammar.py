class Solution:
    def kthGrammer(self,n,k):
        if n == 1:
            return 0
        
        value = self.kthGrammer(n-1, k//2)
        if value:
            value = '10'
        else:
            value = '01'
        
        return int(value[k%2])

    def kthGrammar(self, n: int, k: int) -> int:
        return self.kthGrammer(n,k-1)

       
        