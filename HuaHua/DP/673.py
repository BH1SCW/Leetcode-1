from __future__ import annotations
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        T = [1] * l
        # path = [[] * l]
        n = [0] * l
        for i in range(l):
            for j in range(i):
                if nums[j] < nums[i]:
                    T[i] = max(T[i], T[j] + 1)
            if T[i] == 1:
                n[i] = 1
                continue
            for j in range(i):
                if nums[j] < nums[i] and T[j] == T[i] - 1:
                    # path[i].append(j)
                    n[i] += n[j]
        if not T:
            return 0
        m = max(T)
        indices = [n[i] for i, x in enumerate(T) if x == m]
        return sum(indices)

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,5,4,7]
    nums = [2,2,2,2,2]
    print(sol.findNumberOfLIS(nums))