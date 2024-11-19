class Solution:
    def distanceBetweenBusStops(self, dis: List[int], start: int, des: int) -> int:
        total = sum(dis)
        start, des = min(start,des), max(start,des)
        return min(total-sum(dis[start:des]), sum(dis[start:des]))
