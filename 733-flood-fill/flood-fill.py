class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        len_r, len_c = len(image), len(image[0])

        direction = [[1,0], [0,1], [-1,0], [0,-1]]

        def inbound(r,c):
            return 0 <= r < len_r and 0 <= c < len_c

        original = image[sr][sc]

        q = []
        q.append([sr, sc])

        vis = [[0]*len_c for _ in range(len_r)]
        vis[sr][sc] = 1

        while q:
            
            row, col = q.pop()
            image[row][col] = color

            for r,c in direction:

                new_r, new_c= row + r, col + c

                if not inbound(new_r, new_c):
                    continue

                if not vis[new_r][new_c] and image[new_r][new_c] == original:
                    q.append([new_r, new_c])
                    vis[new_r][new_c] = 1

        return image


        