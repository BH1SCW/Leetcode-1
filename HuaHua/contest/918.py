from __future__ import annotations


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def cross(arr):
            s = sum(arr)
            l = len(arr)
            # starts with first element
            v0 = [arr[0]] + [0] * (l - 1)
            for i in range(1, l):
                v0[i] = v0[i - 1] + arr[i]
            # ends with last element
            v1 = [0] * (l - 1) + [arr[-1]]
            for i in range(l - 2, -1, -1):
                v1[i] = v1[i + 1] + arr[i]
            # store
            m = arr[0]
            T = [[0] * l for i in range(l)]
            for i in range(l):
                for j in range(i, -1, -1):
                    if i == j:
                        T[i][j] = s
                    else:
                        T[i][j] = v1[i] + v0[j]
                    if T[i][j] > m:
                        m = T[i][j]
            return m
        def helper(A):
            l = len(A)
            T = [[0] * l for i in range(l)]
            m = A[0]
            for i in range(0, l):
                for j in range(i, -1, -1):
                    if i == j:
                        T[i][j] = A[j]
                    else:
                        T[i][j] = T[i][j + 1] + A[j]
                    if T[i][j] > m:
                        m = T[i][j]
            return m
        return max(helper(A), cross(A))


if __name__ == '__main__':
    sol = Solution()
    s = [2,-2,2,7,8,0]
    s = [-2,-3,-1]
    s = [3,-2,2,-3]
    s = [5,-3,5]
    s = [1, -2, 3, -2]
    s = [3,-1,2,-1]
    print(sol.maxSubarraySumCircular(s))

