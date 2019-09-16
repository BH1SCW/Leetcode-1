from __future__ import annotations

class Solution:
    def maxSubarray(self, A: List[int]) -> int:
        cur_max, max_sum = 0, A[0]
        for a in A:
            cur_max = max(cur_max + a, a)
            max_sum = max(max_sum, cur_max)
        return max_sum



if __name__ == '__main__':
    sol = Solution()
    s = [-2,-3,-1]
    s = [3,-2,2,-3]
    s = [5,-3,5]
    s = [3,-1,2,-1]
    s = [2,-2,2,7,8,0]
    s = [-2,4,-5,4,-5,9,4]
    s = [1, -2, 3, -2]
    print(sol.maxSubarray(s))
