class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim algo

        n = len(points)
        
        heap = [[0, 0]] # [cost, node]
        vis = set()

        ans = 0

        while len(vis) < n:

            cost, node = heappop(heap)

            if node in vis:
                continue
            
            vis.add(node)
            ans += cost
            x, y = points[node]

            for nei in range(n):

                if nei not in vis:

                    xi, yi = points[nei]
                    dis = abs(x - xi) + abs(y - yi)
                    heappush(heap, [dis, nei])
        
        return ans






