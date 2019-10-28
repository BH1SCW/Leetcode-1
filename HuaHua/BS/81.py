from __future__ import annotations
def find_pivot(nums):
    l, h = 1, len(nums) - 1
    while l <= h:
        m = (l + h) // 2
        if nums[m - 1] > nums[m]:
            return m
        elif nums[m] > nums[-1]:
            l = m + 1
        elif nums[m] == nums[-1] == nums[0] and sum(nums[:m]) == nums[0] * m:
            l = m + 1
        else:
            h = m - 1
    return 0

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        P = find_pivot(nums)
        N = len(nums)
        l, h = 0, N - 1
        while l <= h:
            m = (l + h) // 2
            if nums[(m + P) % N] == target:
                return True
            elif nums[(m + P) % N] < target:
                l = m + 1
            else:
                h = m - 1
        return False

if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(sol.search(nums, target))
    nums = [3, 3, 1, 2, 3, 3]
    target = 0
    print(sol.search(nums, target))
    target = 2
    print(sol.search(nums, target))
    target = 3
    print(sol.search(nums, target))
    # nums = [2, 3, 1]
    # print(find_pivot(nums))
    # nums = [1, 2, 3]
    # print(find_pivot(nums))
    # nums = [3, 1, 2]
    # print(find_pivot(nums))
    # nums = [3, 3, 1, 2, 3, 3]
    # print(find_pivot(nums))
    # nums = [4, 4, 1, 2, 3, 3]
    # print(find_pivot(nums))
