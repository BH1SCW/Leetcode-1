from __future__ import annotations
class Solution:
    # 这题的边界条件比较难弄
    def findIntegers(self, num: int) -> int:
        ans = 0
        s0 = 1
        s1 = 0
        num += 1
        while num:
            s0, s1 = s0 + s1, s0
            if num & 1 and num & 2:
                ans = 0
            if num & 1:
                ans += s0
            num >>= 1
        return ans



if __name__ == '__main__':
    sol = Solution()
    n = 3
    print(sol.findIntegers(n))
    n = 4
    print(sol.findIntegers(n))
    n = 5
    print(sol.findIntegers(n))
    n = 6
    print(sol.findIntegers(n))
