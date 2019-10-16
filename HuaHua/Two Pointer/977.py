class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i, j, k = 0, len(A) - 1, len(A) - 1
        ans = [0] * len(A)
        while i < j:
            a, b = A[i] * A[i], A[j] * A[j]
            if a >= b:
                ans[k] = a
                i += 1
            else:
                ans[k] = b
                j -= 1
            k -= 1
        ans[0] = A[i] * A[i]
        return ans


