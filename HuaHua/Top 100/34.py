from __future__ import annotations
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(x):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if x < nums[mid]: high = mid
                else: low = mid + 1
            return low
        last = search_left(target) - 1
        if last == -1 or nums[last] != target: return [-1, -1]
        first = search_left(target - 1)
        return [first, last]

    # 这道题看上去虽然简单，但是还是边界条件比较复杂的，而且二分法我的写法并不是最好的
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        low, high = -1, len(nums)
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid
        if low + 1 < len(nums) and nums[low + 1] == target:
            ans[0] = low + 1
        low, high = -1, len(nums)
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid
        if 0 <= low < len(nums) and nums[low] == target:
            ans[1] = low
        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = []
    target = 8
    print(sol.searchRange(nums, target))
    nums = [5]
    target = 5
    print(sol.searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 4
    print(sol.searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 11
    print(sol.searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10, 11]
    target = 5
    print(sol.searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10, 11]
    target = 10
    print(sol.searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(sol.searchRange(nums, target))
