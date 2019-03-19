#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
def isSame(s):
    return s[0] == s[1] and s[1] == s[2]
def isAABB(s):
    return s[0] == s[1] and s[2] == s[3]

def StringReduce(s, lb):
    i = lb
    while True:
        if i + 3 > len(s):
            break
        if isSame(s[i : i + 3]):
            s = s[0 : i] + s[i + 1:]
            continue
        if i + 4 > len(s):
            break
        if isAABB(s[i : i + 4]):
            s = s[0 : i + 3] + s[i + 4:]
            continue
        i += 1
    return s




if __name__ == "__main__":
    # 读取第一行的n
    line = "helloo"
    line = "woooooow"
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        print(StringReduce(line, 0))
    print(StringReduce(line, 0))
