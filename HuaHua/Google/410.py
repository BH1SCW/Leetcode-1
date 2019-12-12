import math
class Solution(object):
    def splitArray(self, nums, m):
        def can_split(target):
            count,  cur = 1, 0
            for i, n in enumerate(nums):
                cur += n
                if cur > target: count, cur = count + 1, n
                if count > m or n > target: return False
            return True
        low, high = min(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1
        return low

    def splitArray2(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[math.inf] * n for _ in range(m + 1)]
        s = [[0] * n for _ in range(n)]
        for i in range(n)[::-1]:
            s[i][i] = nums[i]
            for j in range(i + 1, n):
                s[i][j] = s[i][j - 1] + nums[j]
        for i in range(n):
            dp[1][i] = s[i][n - 1]
        for k in range(2, m + 1):
            for i in range(n - k + 1)[::-1]:
                for j in range(i, n - k + 1):
                    dp[k][i] = min(dp[k][i], max(dp[k - 1][j + 1], s[i][j]))
        return dp[k][0]


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(sol.splitArray(nums, m))
    nums = [1, 2147483647]
    m = 2
    print(sol.splitArray(nums, m))

