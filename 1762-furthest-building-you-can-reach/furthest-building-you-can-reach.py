class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        

        heap = []
        n = len(heights)
        i = 0
       

        while i < n-1:

            if heights[i+1] > heights[i]:

                bricks -= ( heights[i+1] - heights[i] )
                heappush(heap, -(heights[i+1] - heights[i]) )

                if bricks < 0:
                    if ladders:
                        bricks -= heappop(heap)
                        ladders -= 1

                    else:
                        return i
            i += 1
            
        return i