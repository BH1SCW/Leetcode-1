from __future__ import annotations
from collections import defaultdict
class Solution:
    # 这个的dp还挺不明显的，花了一会时间才想出来，其实代码还可以继续精简，用数组代替字典，还有就是一开始可以mod，减少存储的空间。
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        state = defaultdict(int)
        for i in range(1, 7):
            state[i, 1] = 1
            state[i] = 1
        for ni in range(2, n + 1):
            new = defaultdict(int)
            for i in range(1, 7):
                # 结尾是i, 1
                for j in range(1, 7):
                    if j != i:
                        new[i, 1] += state[j]
                new[i] = new[i, 1]
                for j in range(2, rollMax[i - 1] + 1):
                    if j > ni:
                        break
                    # 结尾是i, j - 1累加到i, j上
                    new[i, j] += state[i, j - 1]
                    new[i] += new[i, j]
            state = new
        ans = 0
        for i in range(1, 7):
            ans += state[i]
        return ans % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()
    n = 2
    rollMax = [1, 1, 1, 1, 1, 1]
    n = 3
    rollMax = [1, 1, 1, 2, 2, 3]
    n = 2
    rollMax = [1, 1, 2, 2, 2, 3]
    print(sol.dieSimulator(n, rollMax))
