from __future__ import annotations


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        n = len(s)
        l = 0
        for w in wordDict:
            if len(w) > l:
                l = len(w)
        T = [0] * n
        for i in range(n):
            for j in range(i, max(i - l, -1), -1):
                if (j == 0 or T[j - 1]) and s[j:i+1] in d:
                    T[i] = 1
                    continue
        return T[-1] == 1

if __name__ == '__main__':
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))


