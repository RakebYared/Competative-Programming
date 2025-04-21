from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = deque()
      
        q.append((0, True))
        q.append((0, False))
        
        ans = [-1] * n

        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]

        for a, b in redEdges:
            red[a].append(b)
    
        for a, b in blueEdges:
            blue[a].append(b)
    
      
        red_vis = [False] * n
        blue_vis = [False] * n

        step = 0

        while q:
            for _ in range(len(q)):
                node, is_red = q.popleft()
                if ans[node] == -1:
                    ans[node] = step

                if is_red:

                    for nei in blue[node]:
                        if not blue_vis[nei]:
                            blue_vis[nei] = True
                            q.append((nei, False))
                else:
                   
                    for nei in red[node]:
                        if not red_vis[nei]:
                            red_vis[nei] = True
                            q.append((nei, True))
            step += 1

        return ans
