from __future__ import annotations
class Solution:
    # 比较活，但是没有什么特别的技术含量在里面
    def minimumSwap(self, s1: str, s2: str) -> int:
        count = {}
        for c1, c2 in zip(s1, s2):
            if c1 == c2: continue
            count[c1] = count.get(c1, 0) + 1
        ans = 0
        ans += count.get('x', 0) // 2
        count['x'] = count.get('x', 0) % 2
        ans += count.get('y', 0) // 2
        count['y'] = count.get('y', 0) % 2
        if count['x'] != count['y']: return -1
        return ans + count['x'] * 2





    def minimumSwap2(self, s1: str, s2: str) -> int:
        ans = 0
        s1, s2 = list(s1), list(s2)
        for i, c1 in enumerate(s1):
            if c1 == s2[i]: continue
            for j in range(i + 1, len(s2)):
                if s1[j] != s2[j] and s2[j] == s2[i]:
                    s1[i], s2[j] = s2[j], s1[i]
                    ans += 1
                    break
            if s1[i] != s2[i]:
                s1[i], s2[i] = s2[i], s1[i]
                ans += 1
            for j in range(i + 1, len(s2)):
                if s1[j] != s2[j] and s2[j] == s2[i]:
                    s1[i], s2[j] = s2[j], s1[i]
                    ans += 1
                    break
            if s1[i] != s2[i]: return -1
        return ans




if __name__ == '__main__':
    sol = Solution()
    s1 = "xy"
    s2 = "yx"
    print(sol.minimumSwap(s1, s2))
    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"
    print(sol.minimumSwap(s1, s2))
    s1 = "xx"
    s2 = "xy"
    print(sol.minimumSwap(s1, s2))
    s1 = "xx"
    s2 = "yy"
    print(sol.minimumSwap(s1, s2))
