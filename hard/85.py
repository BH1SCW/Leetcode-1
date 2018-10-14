class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # if_debug = True
        if not matrix:
            return 0
        w = len(matrix[0])
        l = len(matrix)
        hist_old = [int(i) for i in matrix[0]]
        max_area = largest_area(hist_old)
        hist_current = [0 for i in range(w)]
        for i in range(1, l):
            for j in range(w):
                hist_current[j] = hist_old[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(largest_area(hist_current), max_area)
            hist_current, hist_old = hist_old, hist_current
        return max_area

def largest_area(heights):
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

