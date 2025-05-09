class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:


        if self.max_heap and num < (-1 * self.max_heap[0]):
            heappush(self.max_heap, -1 * num)
        else:
            heappush(self.min_heap, num)


        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -1 * heappop(self.max_heap))
        
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -1 * heappop(self.min_heap))


       

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2

        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()