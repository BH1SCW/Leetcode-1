def getKeyPoints(l):
    result = []
    for i in range(len(l)):
        if i + 1 <= len(l) - 1:
            if l[i + 1][0] == l[i][0]:
                l[i + 1][2] = max(l[i][2], l[i + 1][2])
                continue
        result.append([l[i][0], l[i][2]])
    return result


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        left = sorted(buildings)
        right = sorted(buildings, key=lambda k : k[1])
        result = []
        for i in range(len(left)):
            if i + 1 <= len(left) - 1:
                if left[i + 1][0] == left[i][0]:
                    left[i + 1][2] = max(left[i][2], left[i + 1][2])
                    continue
            result.append([left[i][0], left[i][2]])
        for i in range(len(right) - 1, - 1, - 1):
            if i - 1 <= len(right) - 1:
                if right[i + 1][0] == right[i][0]:
                    right[i + 1][2] = max(right[i][2], right[i + 1][2])
                    continue
            result.append([right[i][0], right[i][2]])







# [[2,9,10], [3,7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]