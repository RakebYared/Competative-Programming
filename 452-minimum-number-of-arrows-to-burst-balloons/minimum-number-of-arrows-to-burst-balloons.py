class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        target = points[0]
        count = 1
        
        for start,end in points:
            if target[1] >= start:
                target[0] = max(start, target[0])
                target[1] = min(end, target[1])
            else:
                count += 1
                target = [start, end]
        
        return count 

        