from __future__ import annotations


class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        [left, right] = toBeRemoved
        for [lb, ub] in intervals:
            # if right <= lb or ub <= left: continue
            # if left <= lb < ub <= right: continue
            if lb < left < right < ub:
                ans.append([right, ub])
                ans.append([lb, left])
            elif lb <= left < right < ub:
                ans.append([right, ub])
            elif lb < left < right <= ub:
                ans.append([lb, left])
            elif left < lb < right < ub:
                ans.append([right, ub])
            elif lb < left < ub < right:
                ans.append([lb, left])
            elif left <= lb < ub <= right:
                continue
            else:
                ans.append([lb, ub])
        return sorted(ans)



if __name__ == '__main__':
    sol = Solution()
    intervals = [[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]]
    toBeRemoved = [-1, 4]
    print(sol.removeInterval(intervals, toBeRemoved))
    intervals = [[0, 2], [3, 4], [5, 7]]
    toBeRemoved = [1, 6]
    print(sol.removeInterval(intervals, toBeRemoved))
    intervals = [[0, 5]]
    toBeRemoved = [2, 3]
    print(sol.removeInterval(intervals, toBeRemoved))

