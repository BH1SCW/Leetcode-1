
from __future__ import annotations
class Solution:
    # 这题不难，但是很麻烦，首先要先合并同义词，其次就是要permutation
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        N = len(synonyms)
        new = [set(syn) for syn in synonyms]
        for i in range(N):
            for j in range(i + 1, N):
                if new[i] & new[j]:
                    new[i] = new[i] | new[j]
                    new[j] = set()
        dic = {}
        sentence = set(text.split())
        for i, syn in enumerate(new):
            for w in syn:
                if w in sentence:
                    dic[w] = syn
        sentence = text.split()
        ans = [sentence]
        for i, word in enumerate(sentence):
            if word in dic:
                copy = ans[:]
                ans.extend([sen[:i] + [syn] + sentence[i + 1:] for sen in copy for syn in dic[word] if syn != word])
        return sorted([' '.join(sen) for sen in ans])


        # 还要考虑 permutation
        # for i, word in enumerate(in_text):
        #     if not word:continue
        #     count = text.count(word)
        #     copy = ans[:]
        #     for c in range(1, count + 1):
        #         for syn in new[i]:
        #             if syn == word: continue
        #             copy.extend([sentence.replace(word, syn, 1) for sentence in copy])
        #     ans.extend(copy)


if __name__ == '__main__':
    sol = Solution()
    synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
    text = "I am happy today but was sad yesterday"
    synonyms = [["v", "yr"]]
    text = "v v v v yZ"
    print(sol.generateSentences(synonyms, text))
