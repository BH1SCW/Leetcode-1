from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        ans, odd = 0, 0
        for k in count:
            ans += count[k]
            if count[k] % 2:
                odd = 1
                ans -= 1
        return ans + odd

