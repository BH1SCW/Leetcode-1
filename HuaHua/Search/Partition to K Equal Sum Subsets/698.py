# author: Xianglong Hu
# speed: beats 99.74%
class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: int) -> bool:
        if sum(nums) % k:
            return False
        if k == 1:
            return True
        used = [0] * len(nums)
        t = int(sum(nums) / k)
        nums.sort(reverse=True)

        def dfs(target, index, used, count):
            if target == 0:
                if count == 1:
                    return True
                else:
                    return dfs(t, 0, used, count - 1)
            for i in range(index, len(nums)):
                if not used[i] and target >= nums[i]:
                    used[i] = 1
                    if dfs(target - nums[i], i + 1, used, count):
                        return True
                    used[i] = 0
            return False

        return dfs(t, 0, used, k)


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    # nums = [2,2,2,2,3,4,5]
    # k = 4
    # nums = [10,10,10,7,7,7,7,7,7,6,6,6]
    # k = 3
    print(sol.canPartitionKSubsets(nums, k))
