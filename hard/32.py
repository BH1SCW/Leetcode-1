# ()()(())(()()()()(()((((()))))
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        max = 0
        i = 0
        prev = ['Null', 0, []]
        valid = True
        while i < len(s):
            # if prev[0] == 'Null':
            if prev[1] == 0:
                prev = [s[i], 1, [i]]
                i += 1
                continue
            if s[i] == '(':
                if prev[0] == '(':
                    prev[1] += 1
                    prev[2].append(i)
                if prev[0] == ')':
                    prev = [s[i], 1, [i]]
            else:
                if prev[0] == '(':
                    prev[1] -= 1
                    prev[2].pop()
                    # if prev[1] == 0:
                    #     prev = [s[i], 1, [i]]
                    n += 1
                if prev[0] == ')':
                    valid = False
                    n = 0
                    if n >= max:
                        max = n
                    prev = [s[i], 1, [i]]
            i += 1
        if n >= max:
            max = n
        return max * 2

