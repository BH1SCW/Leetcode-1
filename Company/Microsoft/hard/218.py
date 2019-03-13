import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        active = []
        inactive = set()
        map = {}
        events = []
        ans = []
        max_height = 0
        for bd in sorted(buildings):
            start, end = (bd[0], -bd[2], 'l'), (bd[1], -bd[2], 'r')
            events.append(start)
            events.append(end)
            map[end] = start
        for e in sorted(events):
            if e[-1] == 'l':
                heapq.heappush(active, (e[1], e[0], e[2]))
                heapq.heapify(active)
            else:
                inactive.add(map[e])
            while active and (active[0][1], active[0][0], 'l') in inactive:
                heapq.heappop(active)
            max_height = - active[0][0] if active else 0
            if ans and ans[-1][0] == e[0]:
                ans[-1] = [e[0], max_height]
            else:
                if not ans or ans[-1][1] != max_height:
                    ans.append([e[0], max_height])
        return ans

if __name__ == '__main__':
    b = [[1, 2, 1]]
    # b = [[1, 3, 1], [2, 4, 2]]
    # b = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    sol = Solution()
    print(sol.getSkyline(b))

