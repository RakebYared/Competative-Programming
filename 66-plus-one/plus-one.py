class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        digits[-1]+=1
        i = len(digits)-1
        while i<len(digits) and digits[i]>9:
            digits[i] = digits[i]-10
            i-=1
            digits[i]+=1
        
        return digits if digits[0]!=0 else digits[1:]

