from __future__ import annotations
class Solution:
    # 因为只要最大值，所以不需要while
    def longestOnes(self, A: List[int], K: int) -> int:
        j = 0
        for i, n in enumerate(A):
            K -= (1 - n)
            if K < 0:
                K += (1 + A[j])
                j += 1
        return i - j + 1

    # 这个是一般的做法，其实这里不需要，因为只要一个最大的window就行了
    def longestOnes(self, A: List[int], K: int) -> int:
        res = j = 0
        for i, n in enumerate(A):
            K -= (1 - n)
            while K < 0:
                K += (1 - A[j])
                j += 1
            res = max(res, i - j + 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    print(sol.longestOnes(A, K))
    A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    K = 3
    print(sol.longestOnes(A, K))
