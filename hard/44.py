class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if len(p) == 0:
            if len(s) != 0:
                return False
            else:
                return True
        if len(s) == 0:
            if len(p) == 1 and p[0] == "*":
                return True
            else:
                return False
        # # ans = [[False] * len(s)] * len(p)
        ans = [[False for i in range(len(s) + 1)] for j in range(len(p))]
        for i in range(len(p)):
            for j in range(len(s) + 1):
                if p[i] == "*":
                    if i == 0:
                        ans[i][j] = True
                        continue
                    if j == 0:
                        continue
                    if i - 1 >= 0 and j - 1 >= 0:
                        # zero occurence
                        ans[i][j] = ans[i - 1][j]
                        # one or more
                        if ans[i - 1][j - 1]:
                            for k in range(j - 1, len(s) + 1):
                                ans[i][k] = True
                            break
                if p[i] == "?":
                    if i == 0:
                        ans[i][1] = True
                        break
                    if i - 1 >= 0 and j - 1 >= 0 and (ans[i - 1][j - 1]):
                        ans[i][j] = True
                        continue
                if p[i] != "*" and p[i] != "?":
                    if i == 0:
                        ans[i][1] = p[i] == s[i]
                        break
                    if i - 1 >= 0 and j - 1 >= 0 and ans[i - 1][j - 1]:
                        ans[i][j] = p[i] == s[j - 1]
        return ans[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    s = 'aa'
    p = 'a'
    s = "aa"
    p = "*"
    s = "cb"
    p = "?a"
    s = "adceb"
    p = "*a*b"
    s = "acd"
    p = "a*c"
    s = "acdcb"
    p = "a*c?b"
    s = "acdc"
    p = "*a*"
    s = "a"
    p = "a*"
    s = "b"
    p = "?"
    s = "ab"
    p = "?*"
    s = "b"
    p = "*?*?"
    print(sol.isMatch(s, p))