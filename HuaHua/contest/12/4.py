from __future__ import annotations
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[N] * N for _ in range(N)]
        for l in range(1, N + 1):
            for j in range(N)[::-1]:
                i = j - l + 1
                if i == j:
                    dp[i][j] = 1
                    continue
                if i < 0: continue
                dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j])
                if i + 1 <= j and arr[i] == arr[i + 1]:
                    dp[i][j] = min(1 + (dp[i + 2][j] if i + 2 <= j else 0), dp[i][j])
                for k in range(i + 2, j + 1):
                    if arr[k] == arr[i]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + (dp[k + 1][j] if k + 1 <= j else 0))
        return dp[0][N - 1]

    def minimumMoves2(self, arr: List[int]) -> int:
        memo = {}
        def dfs(k, l):
            if (k, l) in memo:
                return memo[k, l]
            if k == l:
                return 1
            if k > l:
                return 0
            ans = l - k + 1
            ans = min(ans, dfs(k + 1, l) + 1)
            if arr[k] == arr[k + 1]:
                ans = min(ans, dfs(k + 2, l) + 1)
            for i in range(k + 2, l + 1):
                if arr[i] == arr[k]:
                    ans = min(ans, dfs(k + 1, i - 1) + dfs(i + 1, l))
            memo[k, l] = ans
            return ans
        return dfs(0, len(arr) - 1)


    # 这个应该是对的，但是效率太慢了，参考了别人的写法
    # https://www.geeksforgeeks.org/minimum-steps-to-delete-a-string-after-repeated-deletion-of-palindrome-substrings/
    def minimumMoves2(self, arr: List[int]) -> int:
        s = '_'.join(map(str, arr))
        s = '_' + s + '_'
        memo = {'_' : 0}
        def is_palindrome(s):
            s = s.split('_')
            return s == s[::-1]
        def dfs(s):
            if s in memo:
                return memo[s]
            ans = len(s)
            for i in range(len(s)):
                if s[i] != '_': continue
                for j in range(i + 2, len(s)):
                    if s[j] != '_': continue
                    if is_palindrome(s[i:j + 1]):
                        ans = min(dfs(s[:i] + s[j:]) + 1, ans)
            memo[s] = ans
            return ans
        return dfs(s)

if __name__ == '__main__':
    sol = Solution()
    arr = [10,15,20,1,18,13,2,2]
    print(sol.minimumMoves(arr))
    arr = [1, 3, 4, 1, 5]
    print(sol.minimumMoves(arr))
    arr = [16,13,13,10,12]
    print(sol.minimumMoves(arr))
    arr = [1, 2]
    print(sol.minimumMoves(arr))
    arr = [1,14,18,20,14]
    print(sol.minimumMoves(arr))
