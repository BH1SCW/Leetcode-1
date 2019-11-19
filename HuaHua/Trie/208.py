from __future__ import annotations
import string
# 这个属于不是很正统的方法，严格按照正统的prefix tree参照
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58989/My-python-solution
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.dic
        for c in word:
            trie = trie.setdefault(c, {})
        trie['*'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.dic
        for c in word:
            if not trie: break
            trie = trie.get(c, {})
        return '*' in trie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.dic
        for c in prefix:
            if not trie: break
            trie = trie.get(c, {})
        return len(trie) > 0

    def find_word(self, prefix, trie, k, ans):
        if len(ans) == k: return
        if '*' in trie:
            ans.append(prefix)
        if not trie: return
        for c in string.ascii_lowercase:
            if c in trie:
                self.find_word(prefix + c, trie.get(c, {}), k, ans)


    def autocomplete(self, word, low, k):
        ans = []
        sub = self.dic
        for i, c in enumerate(word):
            sub = sub.get(word[i], {})
            if i < low - 1: continue
            sugguestions = []
            self.find_word(word[:i + 1], sub, k, sugguestions)
            ans.append(sugguestions)
        return ans



if __name__ == '__main__':
    trie = Trie();
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    trie = Trie();
    numProducts = 5
    repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    customerQuery = "mouse"
    for w in repository:
        trie.insert(w)
    print(trie.autocomplete(customerQuery, 2, 3))

