from __future__ import annotations
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            if m >= len(nums): break
            m = max(i + n, m)
        return True

    # 这个的复杂度我分析错了，应该是O(n+k), k is the sum of the arry, 我一开始以为是O(n)，所以最后由两个test case没过，事实上这道题只需要关注最远能到达的地方，而不需要知道每个点
    def canJump2(self, nums: List[int]) -> bool:
        if not nums: return False
        nums[-1] = 1
        for i in range(len(nums) - 1)[::-1]:
            n = nums[i]
            if i + n >= len(nums) - 1:
                nums[i] = 1
                continue
            for k in range(1, n + 1):
                if i + k >= len(nums): continue
                if nums[i + k]:
                    nums[i] = 1
                    continue
        return nums[0] > 0

if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))
