from __future__ import annotations

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        def palindromes(s):
            ans = [(s[0], s[1:])]
            for i in range(2, len(s) + 1):
                if is_palindrome(s[:i]):
                    ans += [(s[:i], s[i:])]
            return ans
        ans = []
        def search(tail, path):
            if not tail:
                ans.append(path)
                return
            partitions = palindromes(tail)
            # print(partitions)
            for p in partitions:
                search(p[1], path + [p[0]])
        search(s, [])
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "aab"
    print(sol.partition(s))
