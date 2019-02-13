class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        T = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    T[i] = max(T[i], T[j] + 1)
            res = max(res, T[i])
        return res