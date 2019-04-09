# author: Xianglong Hu
# speed: beats 19%
class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: int) -> bool:
        if sum(nums) % k:
            return False
        if k == 1:
            return True
        used = [0] * len(nums)
        target = int(sum(nums) / k)
        ts = [target] * k
        nums.sort(reverse=True)

        def dfs(ts, ind, used, count):
            if ind == len(nums):
                for g in range(0, k):
                    if ts[g]:
                        return False
                return True
            for g in range(0, k):
                if ts[g] >= nums[ind]:
                    ts[g] -= nums[ind]
                    if dfs(ts, ind + 1, used, count):
                        return True
                    ts[g] += nums[ind]
            return False

        return dfs(ts, 0, used, k)



if __name__ == '__main__':
    sol = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    # nums = [2,2,2,2,3,4,5]
    # k = 4
    # nums = [10,10,10,7,7,7,7,7,7,6,6,6]
    # k = 3
    print(sol.canPartitionKSubsets(nums, k))
