import sys
import math


def numberCoin(coins, m):
    dp = [0] + [math.inf] * m
    for i in range(1, m + 1):
        for c in coins:
            dp[i] = min(dp[i - c] + 1, dp[i])
        for c in coins:
            dp[i] = min(dp[i - c] + 1, dp[i])
    ans = max(dp)
    if ans == math.inf:
        return -1
    else:
        return ans


def minNmberCoin(n, m, coins):
    return numberCoin(coins, m)


if __name__ == "__main__":
    m = 20
    n = 4
    coins = [1, 2, 5, 10]
    print(minNmberCoin(n, m, coins))
    # 读取第一行的n
    line = sys.stdin.readline().strip().split()
    m = int(line[0])
    n = int(line[1])
    coins = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        coins += int(line)
        # 把每一行的数字分隔后转化成int列表
    print(minNmberCoin(n, m, coins))
