# s = "mississippi" len = 11, j
# p = "mis*is*p*." len = 10, i
# i = 0, j = 0
# T[i][j] means whether s[0:i] and s[0:j]
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        T = [[0] * (ls + 1) for i in range(lp + 1)] # T[1][1] corresponds to p[0] and s[0]
        T[0][0] = 1
        for i in range(1, lp):
            for j in range(1, ls):
                # if current is *
                if p[i - 1] == '*':
                    T[i][j] == T[i - 1][j]
                    continue
                # if previous is not * and next is not *
                if (i == lp or p[i] != '*') and (i <= 1 or p[i - 2] != '*'):
                    T[i][j] = T[i - 1][j - 1] and ((p[i - 1] == '.') or (p[i - 1] == s[j - 1]))
                    continue
                # if previous is * and next is not *
                if (i == lp or p[i] != '*') and (i >= 2 and p[i - 2] == '*'):
                    T[i][j] = (T[i - 1][j - 1] or T[i - 2][j - 1]) and ((p[i - 1] == '.') or (p[i - 1] == s[j - 1]))
                    continue
                # if previous is * and next is *
                if (i != lp and p[i] == '*') and (i >= 1 and p[i - 2] == '*'):
                    if j >= 2 and s[j - 1] == s[j - 2]:
                        T[i][j] = (T[i - 1][j - 1] or T[i - 2][j - 1])
                    else:
                        T[i][j] = (T[i - 1][j - 1] or T[i - 2][j - 1]) and ((p[i - 1] == '.') or (p[i - 1] == s[j - 1]))
                    continue
                # if previous is not * and next is *
                if (i != lp and p[i] == '*') and (i <= 1 or p[i - 2] != '*'):
                    if j >= 2 and s[j - 1] == s[j - 2]:
                        T[i][j] = T[i - 1][j - 1]
                    else:
                        T[i][j] = (T[i - 1][j - 1]) and ((p[i - 1] == '.') or (p[i - 1] == s[j - 1]))
                    continue

        return T[-1][-1]
