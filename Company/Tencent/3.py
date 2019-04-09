import math
import sys
def game(n, d, p):
    # (cost, force)
    dp = [[(math.inf, 0) for i in range(n)] for j in range(2)]
    dp[1][0] = (p[0], d[0])
    for i in range(1, n):
        if dp[0][i - 1][1] >= d[i]:
            dp[0][i] = dp[0][i - 1]
        if dp[1][i - 1][1] >= d[i]:
            if dp[1][i - 1][0] < dp[0][i][0]:
                dp[0][i] = dp[1][i - 1]
        dp[1][i] = (dp[0][i][0] + p[i], dp[0][i][1] + d[i])
    return min(dp[0][-1][0], dp[1][-1][0])

if __name__ == "__main__":
    # 读取第一行的n
    # line = "1100"
    # line = '01010'
    # print(StringReduce(line))
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    ds = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    ps = list(map(int, line.split()))
    print(game(n, d, p))

