from collections import Counter
class Solution:
    # 在满足条件的情况下，尽量减小i
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        count, count_set = {}, set()
        i = 0
        res = ""
        for j, c in enumerate(s):
            if not c in target:
                continue
            count[c] = count.get(c, 0) + 1
            if count[c] >= target[c]:
                count_set.add(c)
            if len(count_set) == len(target):
                while not s[i] in count or count.get(s[i]) > target[s[i]]:
                    if s[i] in count:
                        count[s[i]] -= 1
                    i += 1
                if not res or j - i + 1 < len(res):
                    res = s[i: j + 1]
        return res

    # 这个做法是正确的，但是题目t里重复的字符也要考虑
    def minWindow2(self, s: str, t: str) -> str:
        target = set(t)
        count = {}
        i = 0
        res = ""
        for j, c in enumerate(s):
            if not c in target:
                continue
            count[c] = count.get(c, 0) + 1
            if len(count) == len(target):
                while count.get(s[i], 2) > 1:
                    if s[i] in count:
                        count[s[i]] -= 1
                    i += 1
                if not res or j - i + 1 < len(res):
                    res = s[i: j + 1]
        return res

