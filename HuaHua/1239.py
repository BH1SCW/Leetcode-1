from __future__ import annotations
class Solution:
    # 这个也超时了，说明python没法用dfs的方法
    def maxLength(self, arr: List[str]) -> int:
        new = []
        for a in arr:
            n = 0
            for c in a:
                n += 1 << ord(c) - ord('a')
            if bin(n).count('1') == len(c): new.append(n)
        self.ans = 0
        def dfs(i, s):
            self.ans = max(self.ans, bin(s).count('1'))
            for a in new[i:]:
                if not a & s:
                    dfs(i + 1, a | s)
        dfs(0, 0)
        return self.ans

    # 这个在python里面超时了，不知道为什么
    def maxLength3(self, arr: List[str]) -> int:
        arr = [set(a) for a in arr if len(set(a)) == len(a)]
        self.ans = 0
        def dfs(i, s):
            self.ans = max(self.ans, len(s))
            for a in arr[i:]:
                if not a & s:
                    dfs(i + 1, a | s)
        dfs(0, set())
        return self.ans

    def maxLength2(self, arr: List[str]) -> int:
        arr = [set(a) for a in arr if len(set(a)) == len(a)]
        q = [set()]
        ans = 0
        for a in arr:
            for s in q:
                if not a & s:
                    ns = a | s
                    ans = max(ans, len(ns))
                    q.append(ns)
        return ans

if __name__ == '__main__':
    sol = Solution()
    arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
    print(sol.maxLength(arr))
    arr = ["un", "iq", "ue"]
    print(sol.maxLength(arr))
    arr = ["cha", "r", "act", "ers"]
    print(sol.maxLength(arr))
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    print(sol.maxLength(arr))
