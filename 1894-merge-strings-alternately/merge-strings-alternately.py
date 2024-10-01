class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ls=[]
        for i in range(max(len(word1),len(word2))):
            if i<len(word1):
                ls.append(word1[i])
            else: 
                ls.append(word2[i:])
                break
            if i<len(word2):
                ls.append(word2[i])
            else: 
                ls.append(word1[i+1:])
                break        
        return ''.join(ls)

        
