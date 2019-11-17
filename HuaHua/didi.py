from __future__ import annotations
def solution(N):
    # write your code in Python 3.6
    sign = 1 if N >= 0 else -1
    s = str(sign * N)
    for i, c in enumerate(s):
        if int(c) * sign < 5 * sign:
            return int(s[:i] + '5' + s[i:]) * sign
    return int(s + '5') * sign

if __name__ == '__main__':
    N = -999
    print(solution(N))
    N = 999
    print(solution(N))
    N = 222
    print(solution(N))
    N = -222
    print(solution(N))
    N = 0
    print(solution(N))
