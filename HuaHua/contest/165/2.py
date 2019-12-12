from __future__ import annotations
class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = (4 * cheeseSlices - tomatoSlices)
        if 4 * x + 2 * y == tomatoSlices and x + y == cheeseSlices:
            return [x, y]
        return []




if __name__ == '__main__':
    sol = Solution()

