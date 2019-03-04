import math
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = {}
        counter = {}
        missing = set()
        over = set()
        for ch in t:
            if not ch in target:
                target[ch] = 0
                counter[ch] = 0
            target[ch] += 1
            missing.add(ch)
        i, j = 0, 0
        while i < len(s) and not s[i] in target:
            i += 1
        j = i
        I, J = 0, -1
        if i < len(s) and s[i] in target:
            counter[s[i]] += 1
            if counter[s[i]] == target[s[i]]:
                missing.remove(s[i])
        while(i <= j and i < len(s)):
            if len(missing) == 0:
                if J == -1 or j - i < J - I:
                    I, J = i, j
                counter[s[i]] -= 1
                if counter[s[i]] < target[s[i]]:
                    missing.add(s[i])
                i += 1
                while(i < len(s) and not s[i] in target):
                    i += 1
                if i >= len(s):
                    break
                if not len(missing):
                    if J == -1 or j - i < J - I:
                        I, J = i, j
                j += 1
                while(j < len(s) and not s[j] in target):
                    j += 1
                if j >= len(s):
                    break
                counter[s[j]] += 1
                if counter[s[j]] == target[s[j]]:
                    missing.remove(s[j])
                else:
                    over.add(s[j])
                continue
            if len(missing):
                j += 1
                while(j < len(s) and not s[j] in target):
                    j += 1
                if j >= len(s):
                    break
                counter[s[j]] += 1
                if counter[s[j]] >= target[s[j]] and s[j] in missing:
                    missing.remove(s[j])
                # if counter[s[j]] > target[s[j]]:
                #     over.add(s[j])
            # if len(over):
            #     counter[s[i]] -= 1
            #     if counter[s[i]] == target[s[i]]:
            #         over.remove(s[i])
            #     if counter[s[i]] < target[s[i]]:
            #         missing.add(s[i])
            #     i += 1
            #     while(i < len(s) and not s[i] in target):
            #         i += 1
            #     if i >= len(s):
            #         break
        return s[I: J + 1]



if __name__ == '__main__':
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    s = "a"
    t = "aa"
    s = "ab"
    t = "b"
    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    print(sol.minWindow(s, t))
