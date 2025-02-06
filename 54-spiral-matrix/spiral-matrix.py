class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # borders
        t, r, b, l = -1, len(matrix[0]), len(matrix), -1
        ans = []

        while True:
            if len(ans) == len(matrix[0]) * len(matrix):
                break
            for col in range(l+1, r):
                ans.append(matrix[t+1][col])
            t += 1
            
            if t >= b - 1:
                break

            for row in range(t+1,b):
                ans.append(matrix[row][r-1])
            r-=1

            if l >= r - 1:
                break
            
            for c in range(r-1,l,-1):
                ans.append(matrix[b-1][c])
            
            b-=1


            for row in range(b-1,t,-1):
                ans.append(matrix[row][l+1])
            l+=1
        return ans


            

        