from __future__ import annotations
from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        loc = defaultdict(list)
        dp = [1] * len(arr)
        ans = 1
        for i in range(len(arr)):
            if arr[i] - difference in loc:
                dp[i] = dp[loc[arr[i] - difference][-1]] + 1
                ans = max(ans, dp[i])
            loc[arr[i]].append(i)
        return ans

    def longestSubsequence2(self, arr: List[int], difference: int) -> int:
        dp = [1] * len(arr)
        ans = 1
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                if arr[i] - arr[j] == difference:
                    dp[i] = dp[j] + 1
                    ans = max(ans, dp[i])
                    break
        return ans

if __name__ == '__main__':
    sol = Solution()
    arr = [1,5,7,8,5,3,4,2,1]
    difference = -2
    arr = [1, 3, 5, 7]
    difference = 1
    arr = [1, 2, 3, 4]
    difference = 1
    print(sol.longestSubsequence(arr, difference))
