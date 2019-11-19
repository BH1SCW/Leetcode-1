from __future__ import annotations
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        trie = self.trie
        for w in dict:
            sub = trie
            for c in w:
                sub = sub.setdefault(c, {})
            sub['*'] = {}

    def is_in(self, prefix, trie):
        for i, c in enumerate(prefix):
            if not trie: break
            trie = trie.get(c, {})
        return '*' in trie


    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        trie = self.trie
        for i, c in enumerate(word):
            if not trie: break
            for k, t in trie.items():
                if k == c: continue
                if self.is_in(word[i + 1:], t): return True
            trie = trie.get(c, {})
        return False


if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict(["hello", "leetcode"])
    assert obj.search("leetcoded") is False
    assert obj.search("hhllo") is True
    assert obj.search("hello") is False
    assert obj.search("hell") is False
