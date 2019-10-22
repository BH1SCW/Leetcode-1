from __future__ import annotations
import collections
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count, i = {}, 0
        for j, fruit in enumerate(tree):
            count[fruit] = count.get(fruit, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return j - i + 1

    # 这个我虽然写出来了，但是写的不是特别的简洁
    def totalFruit2(self, tree: List[int]) -> int:
        res = i = 0
        count = collections.defaultdict(int)
        basket = set()
        for j, fruit in enumerate(tree):
            if len(basket) < 2:
                basket.add(fruit)
            if fruit in basket:
                count[fruit] += 1
            else:
                a, b = basket
                res = max(count[a] + count[b], res)
                if a == tree[j - 1]:
                    a, b = b, a
                while i < j and count[a] > 0:
                    count[tree[i]] -= 1
                    i += 1
                basket.remove(a)
                basket.add(fruit)
                count[fruit] += 1
        if len(basket) == 1:
            res = n
        if len(basket) == 2:
            a, b = basket
            res = max(count[a] + count[b], res)
        return res

if __name__ == '__main__':
    sol = Solution()
    trees = [0,1,2,2]
    print(sol.totalFruit(trees))
