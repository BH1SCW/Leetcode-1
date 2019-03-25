import math
class Solution:
    def numSquarefulPerms(self, A: 'List[int]') -> int:
        def isSquare(n):
            return int(math.sqrt(n)) == math.sqrt(n)
        nums = A
        nums.sort()
        ans = [[]]
        for ne in nums:
            new = []
            for ae in ans:
                for i in range(len(ae)):
                    if isSquare(ae[i] + ne) and i < len(ae) - 1 and isSquare(ae[i + 1] + ne):
                        new.append(ae[i:] + [ne] + ae[i + 1:])
                    ans = new
                    if not ans:
                        break
        new.append()
