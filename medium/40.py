class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    # 1 1 1 1
    # 0, 4, dfs(4, 1), [1]
    # 1, 4, dfs(4, 1), [1, 1]
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)

if __name__ == '__main__':
    sol = Solution()
    s = 10
    t = 3
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(sol.combinationSum2(candidates, target))
