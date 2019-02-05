class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        dict = set()
        searched = {}
        final = []
        n = 0
        for w in wordDict:
            n = max(len(w), n)
            dict.add(w)
        def bfs(sentence):
            # print("sentence: {}\tprevious: {}".format(sentence, previous))
            if not sentence:
                return [""]
            if sentence in searched:
                return searched[sentence]
            result = []
            for i in range(1, min(n + 1, len(sentence) + 1)):
                if sentence[:i] in dict:
                    result += [sentence[:i] + " " + r if r else sentence[:i] + r for r in bfs(sentence[i:])]
            searched[sentence] = result
            return result
        return bfs(s)

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))



