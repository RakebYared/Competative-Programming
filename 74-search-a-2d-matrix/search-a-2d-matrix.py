class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        stack=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    return True
                
        return False