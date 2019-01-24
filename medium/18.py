# Important: the data saving is fussy, better use immutable data
global searched
searched = {}
def findKSum(nums, num, target):
    # nums is already sorted
    global searched
    result = []
    # if len(nums) == 1 and num == 1 and target == -2:
    #     print(num)
    if len(nums) == 0:
        return result
    if len(nums) == 1:
        if num == 1 and nums[0] == target:
            result.append(nums)
        searched[(len(nums), num, target)] = result
        # if result:
        #     print("List: {}".format(nums))
        #     print("Number: {}. Sum: {}. Result: {}".format(num, target, result))
        return result
    # for j in range(len(nums) - 1, -1, -1):
    j = len(nums) - 1
    if num == 1:
        for k in range(len(nums)):
            if nums[k] == target:
                result.append([nums[k]])
            searched[(len(nums), num, target)] = result
        return result
        # continue
    if not (j, num - 1, target - nums[j]) in searched:
        temp = findKSum(nums[ : j], num - 1, target - nums[j])
    else:
        temp = searched[(j, num - 1, target - nums[j])]
    if len(temp) and len(temp[0]) == num - 1:
        temp = [i + [nums[j]] for i in temp]
        result += temp
    # if len(nums) > 1 and nums[-1] == nums[-2]:
    #     searched[(len(nums), num, target)] = result
    #     return result
    if not (j, num, target) in searched:
        temp = findKSum(nums[:j], num, target)
        # searched[(j, num, target)] = temp
    else:
        # if num != 4:
        temp = searched[(j, num, target)]
        # else:
        #     temp = []
    if len(temp) and len(temp[0]) == num:
        result += temp
    searched[(len(nums), num, target)] = result
    # if result:
    #     print("List: {}".format(nums))
    #     print("Number: {}. Sum: {}. Result: {}".format(num, target, result))
    return result


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global searched
        nums = sorted(nums)
        answer = []
        # for i in range(len(nums) - 1, -1, -1):
        for i in range(len(nums) - 1,len(nums) -2, -1):
            if not (i, 3, target - nums[i]) in searched:
                temp = findKSum(nums[: i], 3, target - nums[i])
                searched[(i, 3, target - nums[i])] = temp
            else:
                temp = searched[(i, 3, target - nums[i])]
            if len(temp):
                temp = [t + [nums[i]] for t in temp]
                answer += temp
            if not (i, 4, target) in searched:
                temp = findKSum(nums[ : i], 4, target)
                searched[(i, 4, target)] = temp
                answer += temp
            # else:
            #     temp = searched[(i, 4, target)]
            # if len(temp):
        searched = {}
        answer.sort()
        return answer

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    nums = [0, 0, 0, 0]
    # nums =[-3,-2,-1,0,0,1,2,3]
    nums = [1,0,-1,0,-2,2]
    nums.sort()
    # final = findKSum(nums[:3], 2, -2)
    final = sol.fourSum(nums, 0)
    print("{} Answers: {}".format(len(final), final))
    # print(searched)





