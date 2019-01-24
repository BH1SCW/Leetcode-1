def findSum(nums, index, used, target):
    if index < 0:
        return False
    if not used[index] and nums[index] == target:
        used[index] = True
        return True
    if target - nums[index] > 0:
        if not used[index] and findSum(nums, index - 1, used, target - nums[index]):
            used[index] = True
            return True
    # else:
    if findSum(nums, index - 1, used, target):
        return True
    return False

class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        used = [False for i in range(len(nums))]
        nums.sort()
        target = sum(nums) / 4
        if sum(nums) % 4 != 0:
            return False
        for i in range(4):
            if not findSum(nums, len(nums) - 1, used, target):
                print(used)
                return False
        return True

if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3, 3, 3, 2]
    nums = [5,5,5,5,4,4,4,4,3,3,3,3]
    sol = Solution()
    print(sol.makesquare(nums))


