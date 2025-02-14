class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
       
        while columnNumber > 0:    
            columnNumber -= 1                  
            ans.append(chr(columnNumber%26 + ord('A')))            
            columnNumber //= 26
               
 
        ans = ans[::-1]

        
        return ''.join(ans) 
        

        