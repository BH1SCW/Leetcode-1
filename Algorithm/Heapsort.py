# Heapsort is interesting, it only takes only O(n) time to buid a heap.
# After building a heap, it takes only O(1) time to extract maximum and O(lgn) to rebuild the tree.
# So the total time would be O(nlgn)
import random


class Heap:
    def __init__(self, s):
        self.size = len(s)
        self.heap = s

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def maxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if i <= self.size - 1:
            largest = i
            if l <= self.size - 1 and self.heap[l] > self.heap[i]:
                largest = l
            if r <= self.size - 1 and self.heap[r] > self.heap[largest]:
                largest = r
            # exchange s[i] and s[largest]
            # Important: only exchange when largest is not i, otherwise the recursion would never stop. From another
            #   side, this means the we no longer need to max-heapify because it has already met the conditions.
            if largest != i:
                tmp = self.heap[i]
                self.heap[i] = self.heap[largest]
                self.heap[largest] = tmp
                # now maxHeapify largest
                self.maxHeapify(largest)

    def buildMaxHeap(self):
        # Important: the second should be -1 instead of 0, for range in python is like [start, end)
        for i in range(self.size - 1, -1, -1):
            self.maxHeapify(i)

    def extractMax(self):
        if self.size > 0:
            max = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap[self.size - 1]  = max
            self.size -= 1

    def heapSort(self):
        self.buildMaxHeap()
        # extract maximum
        while self.size >= 1:
            self.extractMax()
            self.maxHeapify(0)

def Rand(num, start=0, end=100):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res



if __name__ == '__main__':
    s = [3, 1, 4]
    s = []
    s = [1, 2]
    s = [16, 14, 10, 8, 7, 9, 3]
    s = [4 ,16, 10, 14, 7]
    s = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = Heap(s)
    # h.maxHeapify(0)
    # h.buildMaxHeap()
    h.heapSort()
    print(h.heap)
    s = Rand(10)
    s = Heap(s)
    s.heapSort()
    print(s.heap)
    s = Rand(30)
    s = Heap(s)
    s.heapSort()
    print(s.heap)



