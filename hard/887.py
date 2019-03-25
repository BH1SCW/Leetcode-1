# N floors
# K eggs
# above or equal to the F-th floor, 1 <= F <= N, the eggs will break
# Sample:
# K = 1, N = 2, Ans = 2
# K = 2, N = 6, Ans = 3
# dp[N][K] = dp[i][K], find i such that dp[i][K] is smallest
# for each dp[i][K], maximize the worst case
# dp[N][K] = min_i(dp[i][K])
# dp[i][K] = max_broke(dp[N -i][K], dp[i - 1][K - 1])
# base case:
# dp[N][1] = N
# dp[1][K] = 1
# dp[2][K] = 2
# K = 2, N = 6
# i = 1, if  broke, F=0,   K=1, N=0
#        not broke, F=2-6, K=2, N=5
# i = 2, if  broke, F=0-1, K=1, N=1
#        not broke, F=3-6, K=2, N=4
# i = 3, if  broke, F=0-2, K=1, N=2
#        not broke, F=4-6, K=2, N=3
# i = 4, if  broke, F=0-3, K=1, N=3
#        not broke, F=5-6, K=2, N=2
# i = 5, if  broke, F=0-4, K=1, N=4
#        not broke, F=6,   K=2, N=1
# i = 6, if  broke, F=0-5, K=1, N=5
#        not broke, F=6,   K=2, N=0
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for n in range(N + 1):
            dp[n][1] = n
        for k in range(K + 1):
            dp[1][k] = 1
        for n in range(1, N + 1):
            for k in range(2, K + 1):
                for i in range(2, n + 1):
                    dp[i][k] = dp[i - 1][k - 1]
                for i in range(n, 0, -1):
                    dp[i][k] = max(dp[i][k], dp[n - i][k])
                    print("i: {}, k: {}, n: {}, dp: {}".format(i, k, n, dp[i][k]))
                for i in range(1, n + 1):
                    dp[n][k] = min(dp[n][k], dp[i][k] + 1) if dp[n][k] else dp[i][k] + 1
        return dp[n][k]

if __name__ == '__main__':
    sol = Solution()
    K = 2
    N = 6
    K = 3
    N = 14
    print(sol.superEggDrop(K, N))
