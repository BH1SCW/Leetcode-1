from __future__ import annotations
from collections import defaultdict
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        e = sorted(list(zip(endTime, startTime, profit)))
        es = sorted(endTime)
        dp = defaultdict(int)
        ans = 0
        for et, st, p in e:
            i, j = bisect.bisect(es, et - 1), bisect.bisect(es, st)
            pet, pst = es[i - 1] if i else 0, es[j - 1] if j else 0
            dp[et] = max(dp[et], dp[pet], dp[pst] + p)
            ans = max(ans, dp[et])
        return ans

# [1,2,3,4,6]
# [3,5,10,6,9]
# [20,20,100,70,60]
# [1,1,1]
# [2,3,4]
# [5,6,4]

if __name__ == '__main__':
    sol = Solution()
    # startTime = [1,2,3,3]
    # endTime = [3,4,5,6]
    # profit = [50,10,40,70]
    # print(sol.jobScheduling(startTime, endTime, profit))
    startTime = [3, 5, 3, 7, 4]
    endTime = [10, 8, 8, 10, 9]
    profit = [10, 8, 10, 9, 9]
    print(sol.jobScheduling(startTime, endTime, profit))
