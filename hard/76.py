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
        for ch in t:
            if not ch in target:
                target[ch] = 0
                counter[ch] = 0
            target[ch] += 1
            missing.add(ch)
        i = 0
        while i < len(s) and not s[i] in target:
            i += 1
        j = i
        I, J = 0, -1
        if i < len(s) and s[i] in target:
            counter[s[i]] += 1
            if counter[s[i]] == target[s[i]]:
                missing.remove(s[i])
        while(i <= j and j < len(s)):
            if len(missing):
                j += 1
                while j < len(s):
                    if not s[j] in counter:
                        j += 1
                    else:
                        if not s[j] in missing:
                            counter[s[j]] += 1
                            j += 1
                        else:
                            counter[s[j]] += 1
                            if counter[s[j]] >= target[s[j]]:
                                missing.remove(s[j])
                            break
            else:
                while i < len(s):
                    if not s[i] in counter:
                        i += 1
                    else:
                        if counter[s[i]] > target[s[i]]:
                            counter[s[i]] -= 1
                            i += 1
                            continue
                        if counter[s[i]] == target[s[i]]:
                            if J == -1 or j - i < J - I:
                                I, J = i, j
                            counter[s[i]] -= 1
                            missing.add(s[i])
                            i += 1
                            break
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
