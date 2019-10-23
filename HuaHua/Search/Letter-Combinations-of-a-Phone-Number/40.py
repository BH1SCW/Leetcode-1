class Solution:
    # 这题困难的地方在于如何消减重复，但是我没看到有不需要
    def combinationSum2(self, candidates, target):
        res, prev = {}, None
        for c in sorted(candidates):
            i = i + 1 if c == prev else 1
            for t in range(target + 1, c, -1):
                if t - c * i in res:
                    res[t] = res.get(t, []) + [com + [c] * i for com in res.get(t - c * i, [[]])]
            res[c] = res.get(c, []) + [[c]] if c != prev else res[c]
            prev = c
        return res.get(target, [])

    def combinationSum22(self, candidates, target):
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
            # 这里的玄机就在这个大于号，保证了第一个会被用上
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
    print(sol.combinationSum22(candidates, target))
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(sol.combinationSum22(candidates, target))
    print(sol.combinationSum2(candidates, target))
