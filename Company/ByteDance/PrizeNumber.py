#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
def findLocalMininum(nums, index):
    n = len(nums)
    i = index
    while (True):
        if nums[i] <= nums[(i + 1) % n]:
            i += 1
            i %= n
        else:
            break
    return i

def simplePrizeNumber(n, scores):
    prizes = [1] * n
    for i in range(0, n):
        right = (i + 1) % n
        if scores[right] > scores[i]:
            prizes[right] = prizes[i] + 1
    for i in range(n - 1, -1, -1):
        left = ((i - 1) + n) % n
        if scores[left] > scores[i]:
            prizes[left] = max(prizes[i] + 1, prizes[left])
    return sum(prizes)


def PrizeNumber(n, scores):
    localMin = scores.index(min(scores))
    prizes = [0] * n
    def moveLeft(index):
        while (True):
            left = ((index - 1) + n) % n
            if scores[left] >= scores[index]:
                if scores[left] != scores[index]:
                    prizes[left] = prizes[index] + 1
                index -= 1
                index = (index + n) % n
                continue
            if scores[left] < scores[index]:
                prizes[index] = max(prizes[left] + 1, prizes[index]) if prizes[index] else 0
            return (left + 1) % n
    def moveRight(index):
        while (True):
            right = ((index + 1) + n) % n
            if scores[right] >= scores[index]:
                if scores[right] != scores[index]:
                    prizes[right] = prizes[index] + 1
                index += 1
                index = index % n
                continue
            if scores[right] < scores[index]:
                prizes[index] = max(prizes[right] + 1, prizes[index]) if prizes[index] else 0
            return ((right - 1) + n) % n
    while (True):
        if prizes[localMin]:
            break
        prizes[localMin] = 1
        l, r = moveLeft(localMin), moveRight(localMin)
        localMin = findLocalMininum(scores, r)
    return sum(prizes)










if __name__ == "__main__":
    # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     headCount = int(line)
    #     line = sys.stdin.readline().strip()
    #     scores = list(map(int, line.split()))
    #     print(PrizeNumber(headCount, scores))
    # print(ans)
    n = 2
    scores = [1, 2]
    # n = 4
    # scores = [1, 2, 3, 3]

    # print(PrizeNumber(n, scores))
    print(simplePrizeNumber(n, scores))
