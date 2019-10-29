from __future__ import annotations
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        visited = set()
        for i, c in enumerate(s):
            count[c] -= 1
            if c in visited: continue
            while stack and c < stack[-1] and count[stack[-1]]:
                ch = stack.pop()
                visited.remove(ch)
            visited.add(c) # 这里一开始判断加不加的条件错了，不管怎么样都应该加的
            stack.append(c)
        return "".join(stack)

    # 这个做法其实我能够想到的
    def removeDuplicateLetters2(self, s: str) -> str:
        if not s: return s
        count = Counter(s)
        pos = 0
        for i, c in enumerate(s):
            if c < s[pos]: pos = i
            count[c] -= 1
            if not count[c]: break
        return s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))

if __name__ == '__main__':
    sol = Solution()
    s = "bcabc"
    print(sol.removeDuplicateLetters(s))
    s = "cbacdcbc"
    print(sol.removeDuplicateLetters(s))
    s = "bbbacacca"
    print(sol.removeDuplicateLetters(s))
