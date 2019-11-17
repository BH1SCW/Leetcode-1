from __future__ import annotations
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = []
        ans = list(s)
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if not stack:
                    invalid.append(i)
                else:
                    stack.pop()
        for i in invalid + stack:
            ans[i] = ""
        return "".join(ans)

if __name__ == '__main__':
    sol = Solution()
    s = "lee(t(c)o)de)"
    print(sol.minRemoveToMakeValid(s))
    s = "a)b(c)d"
    print(sol.minRemoveToMakeValid(s))
    s = "))(("
    print(sol.minRemoveToMakeValid(s))
    s = "(a(b(c)d)"
    print(sol.minRemoveToMakeValid(s))
