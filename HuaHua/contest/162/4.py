from __future__ import annotations
from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # words = sorted([(Counter(w), len(w)) for w in words], key=lambda c: c[1], reverse=True)
        N = len(words)
        words = [Counter(w) for w in words]
        word_score = [sum(score[ord(ch) - ord('a')] * word[ch] for ch in word) for word in words]
        self.count = Counter(letters)
        def dfs(i):
            if i > N - 1: return 0
            ans = 0
            word = words[i]
            ans = max(ans, dfs(i + 1))
            if all(self.count.get(ch, 0) >= word[ch] for ch in word):
                self.count -= word
                ans = max(ans, word_score[i] + dfs(i + 1))
                self.count += word
            return ans
        return dfs(0)


    def maxScoreWords2(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # words = sorted([(Counter(w), len(w)) for w in words], key=lambda c: c[1], reverse=True)
        N = len(words)
        words = [Counter(w) for w in words]
        word_score = [sum(score[ord(ch) - ord('a')] * word[ch] for ch in word) for word in words]
        self.count = Counter(letters)
        self.res = 0
        def dfs(i, score):
            self.res = max(self.res, score)
            if i > N - 1: return
            word = words[i]
            if all(self.count.get(ch, 0) >= word[ch] for ch in word):
                self.count -= word
                dfs(i, score + word_score[i])
                self.count += word
        dfs(0, 0)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(sol.maxScoreWords(words, letters, score))
    words = ["xxxz", "ax", "bx", "cx"]
    letters = ["z", "a", "b", "c", "x", "x", "x"]
    score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
    print(sol.maxScoreWords(words, letters, score))
    words = ["leetcode"]
    letters = ["l", "e", "t", "c", "o", "d"]
    score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    print(sol.maxScoreWords(words, letters, score))
    words = ["add", "dda", "bb", "ba", "add"]
    letters = ["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c", "c", "d", "d", "d"]
    score = [3, 9, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(sol.maxScoreWords(words, letters, score))
