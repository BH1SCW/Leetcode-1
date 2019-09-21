from __future__ import annotations

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maximum = 0
        prev = -1
        while i < j:
            if height[i] <= height[j]:
                if height[i] * (j - i) > maximum:
                    maximum = height[i] * (j - i)
                prev = i
                i += 1
            else:
                if height[j] * (j - i) > maximum:
                    maximum = height[j] * (j - i)
                prev = j
                j -= 1
        return maximum

if __name__ == '__main__':
    sol = Solution()
    s = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(s))
