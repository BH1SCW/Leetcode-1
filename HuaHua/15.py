from __future__ import annotations
class Solution:
    # 这道题并没有想象中的那么简单，居然没做出来，唯一的遗憾是不够快
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        index = {n:i for i, n in enumerate(nums)}
        ans = []
        for i, n1 in enumerate(nums):
            if i and nums[i - 1] == n1:
                continue
            for j in range(i + 1, len(nums)): # 这里一开始用enumerate用错了，指标不一致
                n2 = nums[j]
                if j > i + 1 and nums[j - 1] == n2:
                    continue
                if index.get(-(n1 + n2), -1) > j:
                    ans.append([n1, n2, -(n1 + n2)])
        return ans




if __name__ == '__main__':
    sol = Solution()
    nums = [-1, -1, 0, 2]
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))

