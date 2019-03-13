class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        ans = {nums[0]:1, -nums[0]:1} if nums[0] else {0:1}
        nums = nums[1:] if len(nums) > 1 else []
        for n in nums:
            temp = {}
            for d in ans:
                temp[d + n] = temp.get(d + n, 0) + ans.get(d, 0)
                temp[d - n] = temp.get(d - n, 0) + ans.get(d, 0)
            ans = temp
        return ans.get(S, 0)


#   nums=[1, 1, 1, 1, 1], S=3
#   ans = 0 0 0 0 0 1 0 0 0 0 0
#   ans = 0 0 0 0 1 1 1 0 0 0 0
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(sol.findTargetSumWays(nums, S))

