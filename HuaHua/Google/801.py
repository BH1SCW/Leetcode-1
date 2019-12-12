from __future__ import annotations
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        prev_no, prev_swap = 0, 1
        for i in range(N - 1)[::-1]:
            a, b = A[i], B[i]
            no = swap = N
            if a < A[i + 1] and b < B[i + 1]:
                no = min(prev_no, no)
                swap = min(prev_swap, swap) + 1
            if a < B[i + 1] and b < A[i + 1]:
                no = min(prev_swap, no)
                swap = min(prev_no, swap) + 1
            prev_no, prev_swap = no, swap
        return min(no, swap)

if __name__ == '__main__':
    sol = Solution()
    A = [1, 3, 5, 4]
    B = [1, 2, 3, 7]
    print(sol.minSwap(A, B))
