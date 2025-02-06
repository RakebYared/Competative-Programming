class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        direction = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,1],[1,-1],[-1,-1]]
        row = len(img)
        col = len(img[0])
        ans = [[0]*col for _ in range(row)]

        def in_bound(r,c):
            if r<0 or r>=row or c<0 or c>=col:
                return False
            else:
                return True        

        for r in range(row):
            for c in range(col):
                total = img[r][c]
                divider = 9
                for i,j in direction:
                    if in_bound(r+i,c+j):
                        total += img[r+i][c+j]
                    else:
                        divider -= 1
                ans[r][c] = total//divider
        return ans

                
        