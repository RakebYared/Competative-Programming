class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def pattern(strs):
            pattern = [0,0] 
            for i in range(len(strs)-1):
                if i == 0 and strs==strs[0]*len(strs):
                    pattern = [strs[0],len(strs)]
                    break
                else:
                    if strs==strs[:i+1]*(len(strs)//(i+1)):
                        pattern = [strs[:i+1],(len(strs)//(i+1))]
                        break
            return pattern if pattern!=[0,0] else [strs,1]


        pattern1 = pattern(str1)
        pattern2 = pattern(str2)
        
        if pattern1[0] == pattern2[0]:
            return pattern1[0]*math.gcd(pattern1[1],pattern2[1])
        else:
            return ''