from __future__ import annotations
class Solution:
    # 这题做的很简单，我用非常hacky的方法写的，但是还有更加简单的方法，我先不做
    def circularPermutation(self, n: int, start: int) -> List[int]:
        visited = [0] * (2 ** n)
        ans = [0] * (2 ** n)
        def neightbor(num):
            y = 1
            while y < 2 ** n:
                nb = num ^ y
                if 0 <= nb < (2 ** n) and not visited[nb]:
                    yield nb
                y <<= 1
        ans[0], visited[start] = start, 1
        stack = [(start, 1, 0)]
        while stack:
            num, count, seen = stack.pop()
            ans[count - 1] = num
            if count == 2 ** n:
                if start & num == min(start, num):
                    return ans
                continue
            if not seen:
                stack.append((num, count, 1))
                visited[num] = 1
                stack.extend((nb, count + 1, 0) for nb in list(neightbor(num)))
            else:
                visited[num] = 0




    def circularPermutation2(self, n: int, start: int) -> List[int]:
        seen = [0] * (2 ** n)
        def neightbor(num):
            y = 1
            while y < 2 ** n:
                nb = num ^ y
                if 0 <= nb < (2 ** n) and not seen[nb]:
                    yield nb
                y <<= 1
        def dfs(s, count, path):
            if count == 2 ** n:
                if start & s == min(start, s):
                    return path
                return []
            for nb in neightbor(s):
                seen[nb] = 1
                ans = dfs(nb, count + 1, path + [nb])
                if ans:
                    return ans
                seen[nb] = 0
            return []
        seen[start] = 1
        return dfs(start, 1, [start])

if __name__ == '__main__':
    sol = Solution()
    n = 2
    start = 3
    print(sol.circularPermutation(n, start))
    n = 3
    start = 2
    print(sol.circularPermutation(n, start))
    n = 14
    start = 11811
    print(sol.circularPermutation(n, start))
