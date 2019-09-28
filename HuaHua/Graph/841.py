# 这题还是比较简单的，我给的解法其实可以从任意房间出发，没看清题目，题目其实只要从第一个出发就行了
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = set()
        def dfs(n):
            visited.add(n)
            for key_to in rooms[n]:
                if not key_to in visited:
                    dfs(key_to)
                else:
                    start = n
        dfs(0)
        # for r in range(N):
        #     if not r in visited:
        #         dfs(r)
        # visited = set()
        # dfs(start)
        return len(visited) == N

