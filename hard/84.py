class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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

if __name__ == "__main__":
    h = [2,1,5,6,2,3]
    s = Solution()
    s.largestRectangleArea(h)

