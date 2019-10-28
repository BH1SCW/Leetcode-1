from __future__ import annotations
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        i = 0
        max = 0
        while (i <= len(heights)):
            if not s or (i < len(heights) and heights[i] >= heights[s[-1]]):
                s.append(i)
                i += 1
            else:
                j = s.pop()
                area = heights[j] * (i - 1 - s[-1] if s else i)
                max = area if area > max else max
        return max





if __name__ == '__main__':
    sol = Solution()
    heights = [2, 1, 2]
    print(sol.largestRectangleArea(heights))
    heights = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(heights))
    heights = [2,1,5,6,7,8]
    print(sol.largestRectangleArea(heights))

