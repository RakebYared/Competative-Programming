class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        row = len(mat)
        col = len(mat[0])

        for i in range(row):
            for j in range(col):
                diagonal[i+j].append(mat[i][j])

        ans = []
        flag = True

        for val in diagonal.values():
            if flag:
                ans += val[::-1]
                flag = False
            else:
                ans += val
                flag = True
            
        return ans

        