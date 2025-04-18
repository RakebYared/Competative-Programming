class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        ans = []
        
        def backtrack(store, start):

            if len(store) == 4:
                if start == n :
                    ans.append('.'.join(store))
                else:
                    return

            for i in range(start, n):

                num = int(s[start:i+1])

                if num > 255:
                    return 
                
                if start != i and s[start] == '0':
                    return 

                store.append(str(num))
                backtrack(store, i+1)
                store.pop()

           
        backtrack([], 0)
        return ans
