from __future__ import annotations
class Solution:
    # 这题其实很简单。。但是有个小坑想错了，不一定对偶, c1 + c2 != len，这个真的很容易忽略
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def helper(A, B):
            c1 = c2 = 0
            for a, b in zip(A, B):
                if a != A[0] and b != A[0]:
                    return -1
                if a != A[0]:
                    c1 += 1
                if b != A[0]:
                    c2 += 1
            return min(c1, c2)
        a = helper(A, B)
        if a != -1: return a
        return helper(B, A)

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def helper(A, B):
            count = 0
            for a, b in zip(A, B):
                if a == A[0]: continue
                elif b == A[0]:
                    count += 1
                else:
                    return -1
            return min(count, len(A) - count)
        a = helper(A, B)
        if a != -1: return a
        return helper(B, A)

if __name__ == '__main__':
    sol = Solution()
    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    print(sol.minDominoRotations(A, B))
    A = [3, 5, 1, 2, 3]
    B = [3, 6, 3, 3, 4]
    print(sol.minDominoRotations(A, B))
    A = [1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2]
    B = [2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1]
