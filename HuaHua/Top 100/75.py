from __future__ import annotations
class Solution:
    # https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
    # https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    # 我tql了，居然自己想出来饿了这个算法
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i, j, k = 0, 0, N - 1
        while j <= k:
            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
                # 这个是我模仿别人的写法，下面是我自己的想法，本质上是等价的
                # if j < i: j = i
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    nums = [2,0,2,1,1,0]
    print(sol.sortColors(nums))
    nums = [2,2,0, 1,1,0]
    print(sol.sortColors(nums))
    nums = [2,2,0,1,2,0, 1, 0, 2, 2]
    print(sol.sortColors(nums))
    nums = [2, 1]
    print(sol.sortColors(nums))
