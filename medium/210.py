class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ad_list = {}
        # Important: searched and searching is important. searching is to find cycle, searched is  to avoid repeating work.
        searched = {}
        searching = {}
        # construct the map
        for i in range(numCourses):
            ad_list[i] = []
            searched[i] = False
            searching[i] = False
        for p in prerequisites:
                ad_list[p[1]].append(p[0])
        result = []
        global cyclic
        cyclic = False
        def dfs(i):
            global cyclic
            searching[i] = True
            for p in ad_list.get(i):
                if searching[p]:
                    cyclic = True
                if not searched[p] and not searching[p]:
                    dfs(p)
            searched[i] = True
            searching[i] = False
            result.append(i)
        for i in ad_list.keys():
            if not searched[i] and not cyclic:
                dfs(i)
        result.reverse()
        if cyclic:
            return []
        return result

if __name__ == '__main__':
    sol = Solution()
    # sol.findOrder(2, [[1, 0]])
    sol.findOrder(2, [[0, 1]])
    # sol.findOrder(2, [[0, 1], [1, 0]])
