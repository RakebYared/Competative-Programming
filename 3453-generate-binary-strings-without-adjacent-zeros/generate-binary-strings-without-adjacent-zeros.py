class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def backtrack(store, side):

            if len(store) == n:
                ans.append(''.join(store))
                return

            if side:
                store.append('0')
                backtrack(store, False)
                store.pop()

            store.append('1')
            backtrack(store, True)
            store.pop()

        backtrack([], True)
        return ans
            

            
        