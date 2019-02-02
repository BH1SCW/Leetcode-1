# 1 2
# 2 1
# 1 2 3
#
def max_coins(answers, nums):
    if nums in answers:
        return answers[nums]
    result = 0
    for i in range(1, len(nums) - 1):
        result = max(nums[0] * nums[-1] * nums[i] + max_coins(answers, nums[:i + 1]) + max_coins(answers, nums[i:]), result)
    answers[nums] = result
    return result

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answers = {}
        result = max_coins(answers, tuple([1] + nums + [1]))
        return result

if __name__ == '__main__':
    nums = [3,1,5,8]
    nums = [1, 2]
    # nums = [1, 3, 1]
    # nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2,9]
    sol = Solution()
    print(sol.maxCoins(nums))
    # end = time.time()
    # print(end - start)

