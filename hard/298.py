import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: 'int') -> 'None':
        if not self.left:
            heapq.heappush(self.left, -num)
            return
        if len(self.left) > len(self.right):
            if num <= -self.left[0]:
                heapq.heappush(self.left, -num)
                heapq.heapify(self.left)
                t = heapq.heappop(self.left)
                heapq.heappush(self.right, -t)
                heapq.heapify(self.right)
            else:
                heapq.heappush(self.right, num)
                heapq.heapify(self.right)
            return
        if len(self.left) == len(self.right):
            if num >= -self.left[0]:
                heapq.heappush(self.right, num)
                heapq.heapify(self.right)
            else:
                heapq.heappush(self.left, -num)
                heapq.heapify(self.left)
            return
        if len(self.left) < len(self.right):
            if num >= self.right[0]:
                heapq.heappush(self.right, num)
                heapq.heapify(self.right)
                t = heapq.heappop(self.right)
                heapq.heappush(self.left, -t)
                heapq.heapify(self.left)
            else:
                heapq.heappush(self.left, -num)
                heapq.heapify(self.left)
            return



    def findMedian(self) -> 'float':
        if self.left and len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        if len(self.left) > len(self.right):
            return -self.left[0]
        return self.right[0]

if __name__ == '__main__':
    b = [1, 2, 1, -1]
    # b = [[1, 3, 1], [2, 4, 2]]
    # b = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    sol = MedianFinder()
    for i in b:
        sol.addNum(i)
        print(sol.findMedian())


