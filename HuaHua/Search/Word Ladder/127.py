import string
# author: Xianglong Hu
# speed: 98%
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        dict = set(wordList)
        if not endWord in dict:
            return 0
        l = len(beginWord)
        def expand(word, q):
            for i in range(l):
                for c in string.ascii_lowercase:
                    if (word[:i] + c + word[i:] in dict):
                        q.append(word[:i] + c + word[i:])
        step = 0
        q1 = set([beginWord])
        q2 = set([endWord])
        dict.remove(endWord)
        while q1 and q2:
            step += 1
            if (len(q1) > len(q2)):
                q1, q2 = q2, q1
            q = set()
            for word in q1:
                for i in range(l):
                    for c in string.ascii_lowercase:
                        new = word[:i] + c + word[i + 1:]
                        if new in q2:
                            return step + 1
                        if new in dict:
                            q.add(new)
                            dict.remove(new)
            q1 = q
        return 0



if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))



