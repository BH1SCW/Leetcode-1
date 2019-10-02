class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        distance = [abs(ord(se) - ord(te)) for (se, te) in zip(s, t)]
        ans = 0
        for i in range(len(s)):
            if len(s) - i + 1 <= ans:
                return ans
            T = {}
            for j in range(i, len(s)):
                T[j] = T.get(j - 1, 0) + distance[j]
                if T[j] <= maxCost and j - i + 1 > ans:
                    ans = j - i + 1
        return ans



