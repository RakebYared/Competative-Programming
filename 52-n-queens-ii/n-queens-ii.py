class Solution:
    def totalNQueens(self, n: int) -> int:
        
        ans = 0
        placement = [-1]*n

        def issafe(row, col):

            for i in range(row):

                if placement[i] == col or (i + placement[i]) == (row + col) or (i - placement[i]) == (row - col):
                    return False
            
            return True

        def backtrack(row):
            nonlocal ans

            if row == n:
                ans += 1
                return

            for col in range(n):
                if issafe(row, col):
                    placement[row] = col
                    backtrack(row + 1)
        
        backtrack(0)
        
        return ans
 

