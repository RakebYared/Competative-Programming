class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j= 0, 0 
        t, b, r, l= 0, len(matrix), len(matrix[0]), -1
        ans = [matrix[0][0]]
        
        while len(ans) < len(matrix)*len(matrix[0]):
            for j in range(j+1, r):
                ans.append(matrix[i][j])
            r-=1
            for i in range(i+1,b):
                ans.append(matrix[i][j])
            b-=1
            if len(ans) == len(matrix)*len(matrix[0]):
                break
            for j in range(j-1,l,-1):
                ans.append(matrix[i][j])
            l+=1
            for i in range(i-1,t,-1):
                ans.append(matrix[i][j])
            t+=1
        return ans    
