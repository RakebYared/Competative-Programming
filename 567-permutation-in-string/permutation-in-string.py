class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = [0]*26
        counter2 = [0]*26
        k = len(s1)
        n = len(s2)

        for letter in s1:
            counter1[ord(letter) - 97] += 1
        
        for letter in s2[:k]:
            counter2[ord(letter) - 97] += 1
        
        if counter1 == counter2:
            return True 
                    
        for i in range(n-k):
            counter2[ord(s2[i]) - 97] -= 1
            counter2[ord(s2[i + k]) - 97] += 1

            if counter1 == counter2:
                return True 
            
        return False
   

        
       
        