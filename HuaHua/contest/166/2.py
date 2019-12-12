from __future__ import annotations


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        ans = []
        for i, n in enumerate(groupSizes):
            dic.setdefault(n, []).append(i)
            if len(dic[n]) == n:
                ans.append(dic[n])
                dic[n] = []
        return ans



if __name__ == '__main__':
    sol = Solution()
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(sol.groupThePeople(groupSizes))
    groupSizes = [2, 1, 3, 3, 3, 2]
    print(sol.groupThePeople(groupSizes))

