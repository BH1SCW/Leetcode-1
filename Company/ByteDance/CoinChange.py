#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
def CoinChange(total, coins):
    ans = 0
    for c in reversed(coins):
        number = 1
        while (True):
            if number * c <= total:
                number += 1
            else:
                break
        total -= (number - 1) * c
        ans += (number - 1)
    return ans





if __name__ == '__main__':
    for line in sys.stdin:
        price = int(line)
    price = 1024
    price = 0
    price = 200
    ans = CoinChange(1024 - price, [1, 4, 16, 64])
    print(ans)

