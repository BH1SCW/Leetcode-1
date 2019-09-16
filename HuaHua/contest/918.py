from __future__ import annotations


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def cross(arr):
            s = sum(arr)
            l = len(arr)
            # starts with first element
            v0 = [arr[0]] + [0] * (l - 1)
            m0 = [arr[0]] + [0] * (l - 1)
            for i in range(1, l):
                v0[i] = v0[i - 1] + arr[i]
                m0[i] = max(m0[i - 1], v0[i])
            # ends with last element
            v1 = [0] * (l - 1) + [arr[-1]]
            for i in range(l - 2, -1, -1):
                v1[i] = v1[i + 1] + arr[i]
            # store
            m = A[0]
            for i in range(1, l):
                # m1 = max(max(v0[:i]) + v1[i], m)
                m = max(m0[i - 1] + v1[i], m)
            return m
        def helper(A):
            l = len(A)
            T = [0] * l
            T[0] = A[0]
            for i in range(1, l):
                T[i] = max(T[i - 1] + A[i], A[i])
            return max(T)
        return max(helper(A), cross(A))


if __name__ == '__main__':
    sol = Solution()
    s = [-2,-3,-1]
    s = [3,-2,2,-3]
    s = [5,-3,5]
    s = [1, -2, 3, -2]
    s = [3,-1,2,-1]
    s = [2,-2,2,7,8,0]
    s = [-2,4,-5,4,-5,9,4]
    print(sol.maxSubarraySumCircular(s))

