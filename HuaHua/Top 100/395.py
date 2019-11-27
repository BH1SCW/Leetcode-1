from __future__ import annotations
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = [s]
        ans = 0
        while stack:
            new = []
            for sub in stack:
                count = Counter(sub)
                # for..else的用法比较特别，学习了
                # https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/139609/python-iterative-and-recursive-solution
                for ch, v in count.items():
                    if v < k:
                        new.extend(sub.split(ch))
                        break
                else:
                    ans = max(ans, len(sub))
            stack = new
        return ans

    # 这题其实我想复杂了，就是divide and conquer，我其实想到了，但是不够自信，以为是个sliding window的问题
    # 另外这题也可以看做是一个搜索问题，可以有iterative的写法
    def longestSubstring2(self, s: str, k: int) -> int:
        count = Counter(s)
        for ch, v in count.items():
            if v < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        return len(s)
        # if all(v >= k for k, v in count.items()):
        #     return len(s)

if __name__ == '__main__':
    sol = Solution()
    s = "aaabb"
    k = 3
    print(sol.longestSubstring(s, k))
    s = "ababbc"
    k = 2
    print(sol.longestSubstring(s, k))
