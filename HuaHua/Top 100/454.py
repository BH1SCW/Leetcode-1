from __future__ import annotations
import itertools
from collections import defaultdict
class Solution(object):
    # 好吧，我还是第一时间想到了最优解法的，只是表达上不够简洁
    # https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        countAB, countCD = defaultdict(int), defaultdict(int)
        for a, b in itertools.product(A, B):
            countAB[a + b] += 1
        for c, d in itertools.product(C, D):
            countCD[c + d] += 1
        ans = 0
        for k1, v1 in countAB.items():
            ans += countCD[-k1] * v1
        return ans


if __name__ == '__main__':
    sol = Solution()




