class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        columnNumber -= 1   
       
        while columnNumber >= 26:                      
            ans.append(chr(columnNumber%26 + ord('A')))            
            columnNumber //= 26
            columnNumber -= 1   
            
        print(columnNumber)

        

        ans.append(chr(columnNumber + ord('A')))
        ans = ans[::-1]

        
        return ''.join(ans) 
        

        