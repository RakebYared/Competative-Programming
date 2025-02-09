class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        ans = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if image[i][j]:
                    ans[i][col-1-j] = 0
                else:
                    ans[i][col-1-j] = 1
        
        return ans

        