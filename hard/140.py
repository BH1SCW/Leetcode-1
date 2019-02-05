class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        dict = set()
        searched = {}
        final = []
        n = 0
        for w in wordDict:
            n = max(len(w), n)
            dict.add(w)
        def parse(sentence, previous):
            # print("sentence: {}\tprevious: {}".format(sentence, previous))
            if not sentence:
                final.append(previous[:-1])
            for i in range(1, min(n + 1, len(sentence) + 1)):
                if sentence[:i] in dict:
                    parse(sentence[i:], previous + sentence[:i] + " ")
        parse(s, "")
        return final

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))



