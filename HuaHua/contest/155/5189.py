from __future__ import annotations

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = len(text)
        stats = {}
        target = {}
        for s in 'balloon':
            if s in target:
                target[s] += 1
            else:
                target[s] = 1
        for s in text:
            if not s in target:
                continue
            if s in stats:
                stats[s] += 1
            else:
                stats[s] = 1
        for s in target.keys():
            if not s in stats:
                return 0
            ans = min(ans, stats[s] // target[s])
        return ans


if __name__ == '__main__':
    sol = Solution()
    text = "loonbalxballpoon"
    text = "leetcode"
    print(sol.maxNumberOfBalloons(text))
