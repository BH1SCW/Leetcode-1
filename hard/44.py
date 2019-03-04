class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        while len(p) >= 2 and  p[0] == "*" and p[1] == "*":
            p = p[1:]
        if len(p) == 0:
            return not len(s)
        ans = [[False for i in range(len(s) + 1)] for j in range(len(p))]
        # match empty string
        ans[0][0] = p[0] == "*"
        for i in range(len(p)):
            for j in range(1, len(s) + 1):
                if p[i] != "*":
                    if i > 0:
                        ans[i][j] = ans[i - 1][j - 1] and (p[i] == s[j - 1] or p[i] == "?")
                    else:
                        ans[i][1] = p[0] == s[0] or p[0] == "?"
                        break
                else:
                        ans[i][j] = (i > 0 and ans[i - 1][j]) or ans[i][j - 1]
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