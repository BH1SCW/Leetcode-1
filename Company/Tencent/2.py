#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
def StringReduce(s):
    while True:
        reduced = False
        new = ''
        if len(s) <= 1:
            return len(s)
        i = 1
        while i < len(s):
            if s[i] != s[i - 1]:
                i += 2
                if i == len(s):
                    new += s[-1]
            else:
                new += s[i - 1]
                if i == len(s) - 1:
                    new += s[i]
                reduced = True
                i += 1
        s = new
        if not reduced:
            return len(s)



if __name__ == "__main__":
    # 读取第一行的n
    # line = "1100"
    # line = '01010'
    # print(StringReduce(line))
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    print(StringReduce(line))
