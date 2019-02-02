# Important: the data saving is fussy, better use immutable data
# global searched
# searched = {}
def findKSum(nums, index, num, target):
    result = []
    if index + 1 < num:
        return result
    if num == 1:
        for i in range(index + 1):
            if nums[i] == target:
                return [[nums[i]]]
        return result
    # the solution that includes nums[index]
    temp = findKSum(nums, index - 1, num - 1, target - nums[index])
    if temp:
        # result += [t + nums[index] if not nums[index - 1] == nums[index] t[-1] == nums[index]]
        result += [t + [nums[index]] for t in temp]
    # the solution that doesn't include nums[index]
    temp = findKSum(nums, index - 1, num, target)
    if temp:
        # result += [t + nums[index] if not nums[index - 1] == nums[index] t[-1] == nums[index]]
        result += temp
    return result



class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        final = findKSum(nums, len(nums) - 1, 4, target)
        final = [list(j) for j in set([tuple(i) for i in final])]
        return final


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    # nums = [0, 0, 0, 0]
    # nums =[-3,-2,-1,0,0,1,2,3]
    # nums = [1,0,-1,0]
    nums.sort()
    # final = findKSum(nums[:3], 2, -2)
    final = sol.fourSum(nums, 0)
    print("{} Answers: {}".format(len(final), final))
    # print(searched)





