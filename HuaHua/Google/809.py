from __future__ import annotations

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def cut(word):
            j = 0
            ans = []
            for i, ch in enumerate(word):
                if ch == word[j]: continue
                ans.append(word[j:i])
                j = i
            ans.append(word[j:])
            return ans
        target = cut(S)
        ans = len(words)
        for word in words:
            count = cut(word)
            if len(count) != len(target):
                ans -= 1
                continue
            for s1, s2 in zip(count, target):
                if s1[0] != s2[0] or not (len(s2) // len(s1) >= 3) or len(s2)!= len(s1) and len(s2) - len(s1) < 2 * len(s1):
                    ans -= 1
                    break
        return ans

    def expressiveWords2(self, S: str, words: List[str]) -> int:
        m = len(S)
        ans = len(words)
        for word in words:
            i1 = j1 = i2 = j2 = 0
            n = len(word)
            while i1 < n and i2 < m:
                while j1 + 1 < n and word[j1 + 1] == word[i1]:
                    j1 += 1
                while j2 + 1 < m and S[j2 + 1] == S[i2]:
                    j2 += 1
                if S[i2] != word[i1] or (j2 - i2 != j1 - i1 and (j2 - i2 + 1) - (j1 - i1 + 1) < 2):
                    break
                i1, i2 = j1 + 1, j2 + 1
            ans -= int(not(i1 >= n and i2 >= m))
        return ans

if __name__ == '__main__':
    sol = Solution()
    S = "dddiiiinnssssssoooo"
    words = ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso", "dinssoo", "dinso"]
    print(sol.expressiveWords(S, words))
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(sol.expressiveWords(S, words))
    S = "zzzzzyyyyy"
    words = ["zzyy", "zy", "zyy"]
    print(sol.expressiveWords(S, words))
    S = "abcd"
    words = ["abc"]
    print(sol.expressiveWords(S, words))



