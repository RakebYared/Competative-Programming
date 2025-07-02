class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        m = len(pattern)
        ans = []

        for query in queries:

            n = len(query)

            q, p = 0, 0
            flag = True

            while q < n:

                if p < m and query[q] == pattern[p]:                    
                    p += 1

                elif query[q].isupper():
                    flag = False
                    break
                
                q += 1
            
           
            if flag and p == m:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans


        