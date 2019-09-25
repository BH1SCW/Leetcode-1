from __future__ import annotations

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            count = 0
            for elem in nums:
                if elem <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low



if __name__ == '__main__':
    sol = Solution()
    x = [1, 3, 4, 2, 2]
    print(sol.findDuplicate(x))
