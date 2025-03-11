class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        i = 0
        open = 0
        n = len(s)
        ans = 0

        while i < n:
            count = 0
            while i<n and s[i] == ')':
                count = count*2 or 1
                open -= 1
                i += 1
            
            if open:
                count *= (2**open)
            ans += count 
            open += 1
            i += 1

        return ans
