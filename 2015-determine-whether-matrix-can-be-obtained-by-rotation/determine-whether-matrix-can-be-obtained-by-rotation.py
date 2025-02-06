class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        col = len(mat[0])
        row = len(mat)
        if mat == target:
            return True

        for i in range(3):
            temp = [[0]*col for _ in range(row)]
            
            for r in range(row):
                for c in range(col):
                    temp[c][col-1-r] = mat[r][c]
            
            if temp == target:
                return True
            mat = temp
        return False


        