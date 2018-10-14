# ()()(())(()()()()(()((((()))))
# ()()))))()()("
# 2 2 4 4
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # corner case
        if len(s) == 0:
            return 0
        length = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == ')':
                if i - 1 >= 0:
                    if s[i - 1] == '(':
                        if i - 2 >= 0:
                            length[i] = length[i - 2] + 2
                        else:
                            length[i] = 2
                        length[i - 1] = length[i]
                    else:
                        j = i - length[i - 1]
                        if j >= 0:
                            if s[j] == '(':
                                length[i] = length[i - 1] + 2
                                length[j] = length[i]
                                if j - 1 >= 0:
                                    if s[j - 1] == ')':
                                        length[i] += length[j - 1]
                                        length[j] = length[i]
        return max(length)

