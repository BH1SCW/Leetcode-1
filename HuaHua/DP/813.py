from __future__ import annotations

# 有两个比较tricky的地方，一个是不能只用一个向量纪录，不然同一个k会相互干扰
# 指标的上下界一定要定好，最好是inclusive的不要是开区间，不然讨论起来很麻烦
# new和old一定要及时更新，不然还是会和上一轮的结果相互干扰
# 虽然简单，但是实现的时候还是很多坑
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        l = len(A)
        old = [0] * l
        new = [0] * l
        c = 0
        for i in range(l):
            c += A[i]
            old[i] = c / (i + 1)
        for k in range(2, K + 1):
            for i in range(k - 1, l):
                c = sum(A[k - 2:i + 1])
                for j in range(k - 2, i):
                    c -= A[j]
                    new[i] = max(old[j] + c / (i - j), new[i])
            old = new
            new = [0] * l
        return old[-1]

if __name__ == '__main__':
    A = [9,1,2,3,9]
    K = 3
    sol = Solution()
    print(sol.largestSumOfAverages(A, K))

