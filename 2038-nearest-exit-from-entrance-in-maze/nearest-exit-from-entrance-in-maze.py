class Solution:
    def nearestExit(self, grid: List[List[str]], entrance: List[int]) -> int:

        
        len_row, len_col = len(grid), len(grid[0])

        visited = [[0]*len_col for _ in range(len_row)]

        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def inbound(row, col):
            return 0 <= row < len_row and 0 <= col < len_col

        queue = deque() 
        queue.append(entrance)

        row, col = entrance
        visited[row][col] = 1

        steps = -1

        while queue:
            steps += 1
            child = len(queue)
            
            for _ in range(child):
                row, col = queue.popleft()

                for r, c in direction:
                    new_r, new_c = row + r, col + c

                    if not inbound(new_r, new_c):
                        if [row, col] != entrance:
                            return steps
                    else:
                        if grid[new_r][new_c] == '.' and not visited[new_r][new_c]:
                            queue.append([new_r, new_c])
                            visited[new_r][new_c] = 1

        return -1

