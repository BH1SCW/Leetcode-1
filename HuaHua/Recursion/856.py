from __future__ import annotations
class Solution:
    # 基本思路就是这样了，不过确实还是有更简洁的做法,这题还有recursion的做法，其实也不难想到
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        isBracket = lambda x: x == '(' or x == ')'
        for b in S:
            if b == '(':
                stack.append(b)
            else:
                if isBracket(stack[-1]):
                    stack[-1] = 1
                else:
                    stack.pop(-2)
                    stack[-1] *= 2
                if len(stack) >= 2 and not isBracket(stack[-1]) and not isBracket(stack[-2]):
                    stack[-2] += stack[-1]
                    stack.pop()
        return sum(stack)

    # 虽然过了，但是很慢
    def scoreOfParentheses2(self, S: str) -> int:
        stack = []
        isBracket = lambda x: x == '(' or x == ')'
        for b in S:
            if b == '(':
                stack.append(b)
            else:
                s = stack.pop()
                if isBracket(s):
                    if stack and not isBracket(stack[-1]):
                        stack[-1] += 1
                    else:
                        stack.append(1)
                else:
                    stack.pop() # remove a left brac
                    if stack and not isBracket(stack[-1]):
                        stack[-1] += 2 * s
                    else:
                        stack.append(2 * s)
        return sum(stack)

if __name__ == '__main__':
    sol = Solution()
    nums = "(()(()))"
    print(sol.scoreOfParentheses(nums))
