from __future__ import annotations

class Solution:
    # 这题应该还有提高的空间
    def encode(self, num: int) -> str:
        if not num: return ''
        num += 1
        n = len(bin(num)) - 2
        pre = 2 ** n
        while num < pre:
            n -= 1
            pre = 2 ** n
        ans = bin(num - pre)[2:]
        return (n - len(ans)) * '0' + ans


if __name__ == '__main__':
    sol = Solution()
    for n in range(8):
        print(sol.encode(n))
