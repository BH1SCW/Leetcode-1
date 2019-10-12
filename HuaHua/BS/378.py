from __future__ import annotations
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        for _ in range(k):
            v, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return v

