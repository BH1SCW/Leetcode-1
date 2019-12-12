from __future__ import annotations
class Solution:
    def checkRecord(self, n: int) -> int:
        N = 10 ** 9 + 7
        num_states = 7
        prev = [1, 0, 1, 1, 0, 0, 0]
        # 0: starts with one late no ab, 1: starts with two late no ab, 2: starts with present no ab
        # 3: starts with absent 4: starts with one late with absent, 5: starts with two late with absent
        # 6: starts with present with absent
        for _ in range(n - 1):
            cur = [0] * num_states
            cur[0] = prev[2]
            cur[1] = prev[0]
            cur[2] = prev[0] + prev[1] + prev[2]
            cur[3] = cur[2]
            cur[4] = prev[3] + prev[6]
            cur[5] = prev[4]
            cur[6] = prev[3] + prev[4] + prev[5] + prev[6]
            prev = [k % N for k in cur]
        return sum(cur) % N
        so

        # 0 = 2
        # 1 = 0
        # 2 = 0 + 1 + 2
        # 3 = 0 + 1 + 2
        # 4 = 3 + 6
        # 5 = 4
        # 6 = 3 + 4 + 5 + 6
        #

if __name__ == '__main__':
    sol = Solution()
    print(sol.checkRecord(3))
    n = 2
    print(sol.checkRecord(n))
