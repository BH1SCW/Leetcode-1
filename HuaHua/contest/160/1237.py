class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1001):
            if customfunction.f(x, 1) > z:
                break
            for y in range(1, 1001):
                v = customfunction.f(x, y)
                if v == z:
                    ans.append([x, y])
                elif v > z:
                    break
        return ans

