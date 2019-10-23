from __future__ import annotations
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i, budget = 0, maxCost
        dis = lambda c1, c2: abs(ord(c1) - ord(c2))
        for j, (c1, c2) in enumerate(zip(s, t)):
            budget -= dis(c1, c2)
            if budget < 0:
                budget += dis(s[i], t[i])
                i += 1
        return j - i + 1

    # 这个是好久之前做的，其实也是sliding window，但是我一开始做的是最原始的暴力法O(n^2)，今天改进
    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        distance = [abs(ord(se) - ord(te)) for (se, te) in zip(s, t)]
        ans = 0
        for i in range(len(s)):
            if len(s) - i + 1 <= ans:
                return ans
            T = {}
            for j in range(i, len(s)):
                T[j] = T.get(j - 1, 0) + distance[j]
                if T[j] <= maxCost and j - i + 1 > ans:
                    ans = j - i + 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    print(sol.equalSubstring(s, t, maxCost))
    s = "abcd"
    t = "cdef"
    maxCost = 3
    print(sol.equalSubstring(s, t, maxCost))
    s = "abcd"
    t = "acde"
    maxCost = 0
    print(sol.equalSubstring(s, t, maxCost))
    s = "abcd"
    t = "djjj"
    maxCost = 1
    print(sol.equalSubstring(s, t, maxCost))
