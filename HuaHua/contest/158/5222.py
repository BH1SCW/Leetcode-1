class Solution:
    # 这道题其实很简单，就是贪心，不过我想多了。因为他给的string一定也是balanced，所以贪心一定有解
    def balancedStringSplit(self, s: str) -> int:
        ans, l, r = 0, 0, 0
        for c in s:
            if c == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                ans += 1
                l, r = 0, 0
        return ans

