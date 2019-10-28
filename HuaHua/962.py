from __future__ import annotations
import math
class Solution:
    # 不知道为啥，这个memory usage 100%，但是速度只有5%, 看了一下别人的解法，确实只有
    def maxWidthRamp(self, A: List[int]) -> int:
        index = [math.inf] * 50001
        ans = 0
        for i, a in enumerate(A):
            if index[a] == math.inf:
                index[a] = i
        for i in range(1, len(index)):
            index[i] = min(index[i - 1], index[i])
        for i, a in enumerate(A):
            ans = max(i - index[a], ans)
        return ans


    def maxWidthRamp2(self, A: List[int]) -> int:
        ans = 0
        for i, a in enumerate(A):
            for j in range(i):
                if A[j] <= a:
                    ans = max(i - j, ans)
                    break
        return ans

if __name__ == '__main__':
    sol = Solution()
    A = [6,0,8,2,1,5]
    print(sol.maxWidthRamp(A))
    A = [9,8,1,0,1,9,4,0,4,1]
    print(sol.maxWidthRamp(A))
