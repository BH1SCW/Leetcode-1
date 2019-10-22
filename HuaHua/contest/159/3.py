from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
             count[c] -= 1
             while i < n and all(count[ch] <= n / 4 for ch in 'QWER'):
                 res = min(res, j - i + 1)
                 count[s[i]] += 1
                 i += 1
        return res

if __name__ == '__main__':
    sol = Solution()
