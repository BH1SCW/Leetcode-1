import sys
from collections import deque
if __name__ == "__main__":
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    # str1 = "("
    # str2 = ")"
    # str1 = "(("
    # str2 = "))"
    # str1 = "(()"
    # str2 = "())"
    # str1 = "(" # 2
    # str2 = "())"
    # str1 = "()" # 4
    # str2 = "()"
    # str1 = "((" # 2
    # str2 = "))"
    # str1 = "(()" # 2
    # str2 = ")"
    # str1 = "(()" # 2
    # str2 = ")"
    # str1 = "(()"
    # str2 = "())"
    #
    # str1 = "())"
    # str2 = "("
    searched = {}
    def isLegal(s):
        q = deque([])
        for i in s:
            if i == "(":
                q.append(i)
            else:
                if len(q):
                    q.pop()
                else:
                    return False
        return len(q) == 0
    def dfs(s1, s2):
        key = s1 + ' ' + s2
        if key in searched:
            return searched[key]
        key = s2 + ' ' + s1
        if key in searched:
            return searched[key]
        if not s1:
            if isLegal(s2):
                searched[s1 + ' ' + s2] = 1
                return 1
            else:
                searched[s1 + ' ' + s2] = 0
                return 0
        if not s2:
            if isLegal(s1):
                searched[s1 + ' ' + s2] = 1
                return 1
            else:
                searched[s1 + ' ' + s2] = 0
                return 0
        if s1[0] == ')' and s2[0] == ')':
            searched[s1 + ' ' + s2] = 0
            return 0
        ans = 0
        if s1[0] == '(' and len(s1) > 2 and s1[1] == ')':
            ans += dfs(s1[1:-1], s2)
        if s1[0] == '(' and s1[-1] == ')':
            ans += dfs(s1[1:-1], s2)
        if s1[0] == '(' and s2[0] == ')':
            ans += dfs(s1[1:], s2[1:])
        if s1[0] == '(' and len(s2) > 1 and s2[-1] == ')':
            ans += dfs(s1[1:], s2[0:-1])
        s1, s2 = s2, s1
        if s1[0] == '(' and len(s1) > 2 and s1[1] == ')':
            ans += dfs(s1[1:-1], s2)
        if s1[0] == '(' and s1[-1] == ')':
            ans += dfs(s1[1:-1], s2)
        if s1[0] == '(' and s2[0] == ')':
            ans += dfs(s1[1:], s2[1:])
        if s1[0] == '(' and len(s2) > 1 and s2[-1] == ')':
            ans += dfs(s1[1:], s2[0:-1])
        searched[s1 + ' ' + s2] = ans
        return ans
    ans = dfs(str1, str2)
    print(ans % (10e9 + 7))
