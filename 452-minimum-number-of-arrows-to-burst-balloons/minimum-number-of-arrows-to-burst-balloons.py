class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        target = points[0][1]
        count = 1
        
        for start,end in points:
            if start > target:
                count += 1
                target = end
            target = min(end, target)
             
        
        return count 

        