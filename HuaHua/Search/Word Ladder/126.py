import string
import math
# author: Xianglong Hu
# speed: 91.68%
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        dict = set(wordList)
        if not endWord in dict:
            return []
        l = len(beginWord)
        def expand(word, q):
            for i in range(l):
                for c in string.ascii_lowercase:
                    if (word[:i] + c + word[i:] in dict):
                        q.append(word[:i] + c + word[i:])
        def reconstruct(w, path, ans, word):
            if w == beginWord or w == endWord:
                ans.append(path + [w])
            else:
                # map(lambda x: reconstruct(x, path + [w], ans, word), parents[w])
                if path and w == path[0]:
                    return
                for p in parents[w]:
                    # if path and p == path[0]:
                    #     return
                    reconstruct(p, path + [w], ans, word)
        step = 0
        q1, q2 = set([beginWord]), set([endWord])
        dict.remove(endWord)
        parents = {word:[] for word in dict}
        distance = {word:math.inf for word in dict}
        distance[beginWord], distance[endWord] = 0, 0
        isfound = False
        ans = []
        while q1 and q2 and not isfound:
            step += 1
            if (len(q1) > len(q2)):
                q1, q2 = q2, q1
            q = set()
            for word in q1:
                for i in range(l):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        new = word[:i] + c + word[i + 1:]
                        if new in dict and distance[new] > distance[word]:
                            distance[new] = min(distance[new], step)
                            q.add(new)
                            parents[new].append(word)
                            # dict.remove(new)
                        if new in q2:
                            isfound = True
                            p1, p2 = [], []
                            reconstruct(word, [], p1, beginWord), reconstruct(new, [], p2, endWord)
                            if p2 and p2[0][-1] == beginWord:
                                ans += [b[::-1] + a for a in p1 for b in p2]
                            else:
                                ans += [a[::-1] + b for a in p1 for b in p2]
                            # return step + 1
            q1 = q
            # map(dict.remove, q)
            for e in q:
                dict.remove(e)
        return ans



if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    wordList = ["hot", "dot", "dog", "lot", "log"]
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog", "dot"]
    wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]
    print(sol.findLadders(beginWord, endWord, wordList))



