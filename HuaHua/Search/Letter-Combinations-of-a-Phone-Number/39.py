class Solution:
    def combinationSum(self, candidates, target):
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
    candidates = [2, 2, 3, 6, 7]
    target = 7
    print(sol.combinationSum(candidates, target))
