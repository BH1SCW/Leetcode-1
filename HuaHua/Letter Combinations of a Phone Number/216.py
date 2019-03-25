class Solution:
    def combinationSum3(self, k: int, n: int) -> 'List[List[int]]':
        nums = list(range(1, 10))
        def dfs(k, n, nums, res, path):
            if k == 0:
                if n == 0:
                    res.append(path)
                return
            if len(nums) < k:
                return
            if n > 0 and k > 0:
                dfs(k, n, nums[1:], res, path)
                dfs(k - 1, n - nums[0], nums[1:], res, path + [nums[0]])
        res = []
        dfs(k, n, nums, res, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 7
    k = 3
    n, k = 9, 3
    n, k = 15, 3
    print(sol.combinationSum3(k, n))

