class Solution:
    # 这题和coin change本质上是一样的，说明我之前根本没有好好吃透这道题目，而且我已经想不起来top down的做法怎么做了，看了以前的写法以后才恍然大悟
    def combinationSum(self, candidates, target):
        res = {0 : [[]]}
        for c in sorted(candidates):
            for t in range(c, target + 1):
                if t - c in res:
                    res[t] = res.get(t, []) + [com + [c] for com in res.get(t - c, [[]])]
        return res.get(target, [])


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = list(set(candidates))
        def helper(target, partial, result, index):
            if target == 0:
                result.append(partial)
            if target > 0:
                for i in range(index, len(candidates)):
                    helper(target - candidates[i], partial + [candidates[i]], result, i)
            return
        result = []
        helper(target, [], result, 0)
        return result

if __name__ == '__main__':
    sol = Solution()
    s = 10
    t = 3
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combinationSum(candidates, target))
    candidates = [2, 3, 5]
    target = 8
    print(sol.combinationSum(candidates, target))
