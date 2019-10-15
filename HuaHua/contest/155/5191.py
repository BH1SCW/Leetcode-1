class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        s = sum(arr)
        l = len(arr)
        # ends with last element
        v0 = [0] * (l - 1) + [arr[-1]]
        m0 = l - 1
        for i in range(l - 2, -1):
            v0[i] = v0[i + 1] + arr[i]
            if v0[i] > v0[i + 1]:
                m0 = i
        # starts with first element
        v0 = [arr[0]] + [0] * (l - 1)
        m1 = 0
        for i in range(1, l):
            v0[i] = v0[i - 1] + arr[i]
            if v0[i] > v0[i - 1]:
                m1 = i
        # store
        T = [[0] * l for i in range(l)]
        for i in range(l):
            for j in range(i - 1, -1):
                T[i][j] = T[i - 1][j] + arr[j]





