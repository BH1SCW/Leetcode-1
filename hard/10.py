# s = "mississippi" len = 11, j
# p = "mis*is*p*." len = 10, i
# i = 0, j = 0
# T[i][j] means whether s[0:i] and s[0:j]
class Solution:
    def simpleMatch(self, s, p):
        if len(s) == 0:
            return True
        if p != ".":
            for i in s:
                if i != p:
                    return False
        return True

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        T = [[False] * (ls + 1) for i in range(lp + 1)]  # T[1][1] corresponds to p[0] and s[0]
        T[0][0] = True
        for i in range(1, lp + 1):
            # current is *
            if p[i - 1] == '*':
                for j in range(0, ls + 1):
                    T[i][j] = T[i - 1][j]
                continue
            # next is not *
            if i >= lp or p[i] != '*':
                for j in range(1, ls + 1):
                    T[i][j] = T[i - 1][j - 1] and ((p[i - 1] == '.') or (p[i - 1] == s[j - 1]))
                continue
            # 0 corresponds to empty
            for j in range(0, ls + 1):
                # k occurrence
                if j == 0:
                    T[i][j] = T[i - 1][0]
                    continue
                for k in range(j + 1):
                    if T[i - 1][j - k] and self.simpleMatch(s[j - k : j], p[i - 1]):
                        T[i][j] = True
                        continue

        return T[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    s = 'a'
    p = 'a*'
    print(sol.isMatch(s, p))
