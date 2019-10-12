from __future__ import annotations
class Solution:
    # 这题我没有自己想，一开始我使用的是位置，但是位置有个问题，因为这个数组不是按照位置排序的，所以BST的思路有问题
    # 后来改成了直接用数字，但是我想到怎么保证搜索到的数字可能是个质数？这一点不用担心，因为二分法保证搜索到的是满足条件里面最小的。
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def numSmallerEqual(num):
            ans = 0
            for i in range(1, n + 1):
                ans += min(num // i, m)
            return ans
        l, h = 1, m * n
        # t = lambda x: (x // n + 1) * (x % m + 1)
        while l < h:
            mid = (l + h) // 2
            # num = t(mid)
            if numSmallerEqual(mid) < k:
                l = mid + 1
            else:
                h = mid
        return l


if __name__ == '__main__':
    sol = Solution()
    m, n, k = 2, 3, 6
    m, n, k = 45, 12, 471
    print(sol.findKthNumber(m, n, k))
