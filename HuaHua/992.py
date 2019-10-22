from __future__ import annotations
import collections
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        count, i, min_count, min_i, d = {}, 0, {}, 0, {}
        ans = 0
        # 等于两个一起做，但是非常的丑陋，而且也不是很快，不知道为什么， 看了一下别人的答案，实在是高啊
        for j, a in enumerate(A):
            min_count[a] = min_count.get(a, 0) + 1
            while len(min_count) == K:
                d[min_i] = j
                min_count[A[min_i]] -= 1
                if min_count[A[min_i]] == 0: del min_count[A[min_i]]
                min_i += 1
            if len(count) == K and not a in count:
                ans += sum([j - d[mi] for mi in range(i, min_i + 1) if mi in d])
                while len(count) == K:
                    count[A[i]] -= 1
                    if count[A[i]] == 0:
                        del count[A[i]]
                    i += 1
            count[a] = count.get(a, 0) + 1
        ans += sum([j - d[mi] + 1 for mi in range(i, min_i + 1) if mi in d])
        return ans

    # 是对的，但是超时了，这个helper有问题, 因为是n^2， 其实可以更短
    def subarraysWithKDistinct2(self, A: List[int], K: int) -> int:
        def helper(a, d):
            res = 0
            for j in range(len(a) - 1, -1, -1):
                nd = d.copy()
                for i in range(0, j + 1):
                    if len(nd) < K:
                        break
                    res += 1
                    nd[a[i]] -= 1
                    if nd[a[i]] == 0: del nd[a[i]]
                d[a[j]] -= 1
                if d[a[j]] == 0:
                    return res
            return res

        count, i = {}, 0
        ans = 0
        for j, a in enumerate(A):
            if len(count) == K and not a in count:
                ans += helper(A[i:j], count.copy())
                while len(count) == K:
                    count[A[i]] -= 1
                    if count[A[i]] == 0:
                        del count[A[i]]
                    i += 1
            count[a] = count.get(a, 0) + 1
        ans += helper(A[i:j + 1], count.copy())
        return ans

if __name__ == '__main__':
    sol = Solution()
    A = [1, 2]
    K = 2
    print(sol.subarraysWithKDistinct(A, K))
    A = [1, 2, 1, 2, 3]
    K = 2
    print(sol.subarraysWithKDistinct(A, K))
    A = [1, 2, 1, 3, 4]
    K = 3
    print(sol.subarraysWithKDistinct(A, K))
    A = [1, 2, 1, 3, 4]
    K = 5
    print(sol.subarraysWithKDistinct(A, K))
