class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        n = len(s)
        count = 0
        l_count = 0
        r_count = 0

        for c in s:
            if c == 'R':
                r_count += 1
            else:
                l_count += 1
            
            if r_count == l_count:
                count += 1
                r_count, l_count = 0,0
        
        return count 