from __future__ import annotations

class Solution:
    # 这题的算法并不难，但是主要问题是怎么写的简洁
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        def dfs(i, n1, n2, path, ans):
            if i == len(S):
                ans.append(path)
                return
            p = str(n1 + n2)
            if len(S) - i >= len(p) and S[i: i + len(p)] == p and (n1 + n2) < 2**31 - 1:
                dfs(i + len(p), n2, n1 + n2, path + [n1 + n2], ans)
        for i in range(len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                s1, s2 = S[:i + 1], S[i + 1: j + 1]
                n1, n2 = int(s1), int(s2)
                if str(n1) != s1 or str(n2) != s2: break
                dfs(j + 1, n1, n2, [n1, n2], ans)
                if ans: return ans[0]
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "123456579"
    print(sol.splitIntoFibonacci(s))
    s = "11235813"
    print(sol.splitIntoFibonacci(s))
    s = "112358130"
    print(sol.splitIntoFibonacci(s))
    s = "0123"
    print(sol.splitIntoFibonacci(s))
    s = "1101111"
    print(sol.splitIntoFibonacci(s))
    s = "1011"
    print(sol.splitIntoFibonacci(s))
    s = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    print(sol.splitIntoFibonacci(s))
