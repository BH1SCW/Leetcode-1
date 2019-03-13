class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        target = sum(nums)
        if target % 2 != 0:
            return False
        target /= 2
        target = int(target)
        ans = [True] + [False] * target
        for n in nums:
            for t in range(target, n - 1, -1):
                ans[t] = ans[t - n] or ans[t]
        return ans[-1]
# 1 5 11 5
# target = 11
#           0 1 2 3 4 5 6 7 8 9 10 11
#           1 0 0 0 0 0 0 0 0 0 0  0
#[1]        1 1 0 0 0 0 0 0 0 0 0  0
#[1,5]      1 1 0 0 0 0 6 0 0 0 0  0
#[1,5,11]   1 1 0 0 0 0 6 0 0 0 0  1
#[1,5,11,5] 1 1 0 0 0 0 6 0 0 0 0  1

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, 11, 5]
    print(sol.canPartition(nums))
