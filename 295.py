class MedianFinder:

    def __init__(self):
        self.min_heap = [] # 大半
        self.max_heap = [] # 小半
        

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            tmp = heappop(self.min_heap)
            heappush(self.max_heap, -tmp)
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0])/2
        else:
            return -self.max_heap[0]
        