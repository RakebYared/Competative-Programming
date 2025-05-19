class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = len(s)

        def backtrack(store, start):

            if len(store) == n:
                ans.append(''.join(store))
                return

            for i in range(start, n):
                
                store.append(s[i])
                backtrack(store, i+1)
                store.pop()

                if not s[i].isdigit():
                    store.append(s[i].swapcase())
                    backtrack(store, i+1)
                    store.pop()

        backtrack([], 0)
        return ans
        