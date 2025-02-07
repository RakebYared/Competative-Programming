class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i):
                temp = matrix[i][j]
                c, r = j, i
                for _ in range(4):
                    temp, matrix[c][n-1-r] =matrix[c][n-1-r], temp
                    r, c = c, n-1-r
                

        