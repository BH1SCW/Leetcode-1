import heapq, math
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        h = []
        for [x, y] in points:
            d = math.sqrt(x ** 2 + y ** 2)
            if len(h) < K:
                heapq.heappush(h, (-d, x, y))
            elif -d > h[0][0]:
                heapq.heappushpop(h, (-d, x, y))
        return [[x, y] for d, x, y in h]

if __name__ == '__main__':
    sol = Solution()
    points = [[1, 3], [-2, 2]]
    K = 1
    print(sol.kClosest(points, K))
