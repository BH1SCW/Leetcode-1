class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums.sort()
        # 1 2 2
        # [], [1], [2], [1, 2]
        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i - 1]):
                lb = 0
            #     lb = len(ans) - len(new)
            # else:
            #     lb = 0
            new = []
            for a in ans[lb:]:
                new.append(a + [nums[i]])
            lb = len(ans)
            ans += new
        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,2]
    print(sol.subsets(nums))





