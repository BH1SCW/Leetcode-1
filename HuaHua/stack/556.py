from __future__ import annotations
import bisect
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        stack = []
        for i in range(len(s))[::-1]:
            d = int(s[i])
            if stack and stack[-1] > d:
                pos = bisect.bisect(stack, d)
                d, stack[pos] = stack[pos], d
                ans = int(s[:i] + str(d) + ''.join(map(str, stack)))
                return -1 if ans >> 31 else ans # signed value
            stack.append(d)
        return -1


if __name__ == '__main__':
    sol = Solution()
    n = 12
    print(sol.nextGreaterElement(n))
    n = 112
    print(sol.nextGreaterElement(n))
    n = 1122
    print(sol.nextGreaterElement(n))
    n = 12543
    print(sol.nextGreaterElement(n))
    n = 125430
    print(sol.nextGreaterElement(n))
    n = 21
    print(sol.nextGreaterElement(n))
    n = 1999999999
    print(sol.nextGreaterElement(n))
