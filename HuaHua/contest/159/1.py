class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True
        x1, y1 = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        for i in range(2, n):
            x2, y2 = coordinates[i][0] - coordinates[0][0], coordinates[i][1] - coordinates[0][1]
            if x2 * y1 != x1 * y2:
                return False
        return True

[[0, 1], [0, 2], [0, 3]]
