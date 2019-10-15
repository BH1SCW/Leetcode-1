from __future__ import annotations
from collections import defaultdict
class Solution:
    # 这道题的特点是比较繁琐，corner case比较多，包含了三种情况，我一开始只想到一种。由于过于复杂，最好还是分开陈唯两个函数。其他倒没有什么特殊的技术含量。
    # 贴了一个别人的答案，果然是高手啊， 可以利用元素数量的信息，这样更为聪明一点。
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt,freq,maxF,res = defaultdict(int), defaultdict(int),0,0
        for i,num in enumerate(nums):
            cnt[num] += 1
            freq[cnt[num]-1] -= 1
            freq[cnt[num]] += 1
            maxF = max(maxF,cnt[num])
            if maxF*freq[maxF] == i or (maxF-1)*(freq[maxF-1]+1) == i or maxF == 1:
                res = i + 1
        return res

    def maxEqualFreq2(self, nums: List[int]) -> int:
        ans = 1
        rf = defaultdict(int)
        # f = defaultdict(set)
        f = {}
        def check():
            if len(f) == 2:
                [k1, k2] = sorted(f.keys())
                if k2 - k1 == 1 and len(f[k2]) == 1 or k1 == 1 and len(f[k1]) == 1:
                    return True
            elif len(f) == 1:
                [k1] = f.keys()
                if k1 == 1 or len(f[k1]) == 1:
                    return True
            return False
        for i in range(len(nums)):
            n = nums[i]
            rf[n] += 1
            if rf[n] in f:
                f[rf[n]].add(n)
            else:
                f[rf[n]]= set([n])
            if rf[n] > 1:
                f[rf[n] - 1].remove(n)
                if not len(f[rf[n] - 1]):
                    f.pop(rf[n] - 1)
            if check():
                ans = i
            # if len(f) == 2:
            #     if len(f[rf[n]]) == 1:
            #         ans = i
            #         continue
            #     for k in f:
            #         if k != rf[n] and len(f[k]) == 1:
            #             ans = i
            #     # if rf[n] - 1 in f and len(f[rf[n] - 1]) == 1:
            #     #         ans = i
            #     # if rf[n] + 1 in f:
            #     #     if len(f[rf[n] + 1]) == 1 or len(f[rf[n]]) == 1:
            #     #         ans = i
            # if len(f) == 1 and (1 in f or len(rf) == 1):
            #     ans = i
        return ans + 1


if __name__ == '__main__':
    sol = Solution()
    # nums = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,42,21,45,27,78,39,78,24,47,60,22,33,45,18,56,91,93,66,79,65,43,7,57,63,74,25,11,14,100,95,19,3,22,18,94,52,91,33,95,16,93,63,65,8,88,51,47,7,51,77,36,48,89,72,81,75,13,69,9,31,16,38,34,76,7,82,10,90,64,28,22,99,40,88,27,94,85,43,75,95,86,82,46,9,74,67,51,93,97,35,2,49]
    # print(nums[:23])
    # print(sol.maxEqualFreq(nums))
    # nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
    # print(sol.maxEqualFreq(nums))
    # nums = [2,2,1,1,5,3,3,5]
    # print(sol.maxEqualFreq(nums))
    # nums = [1,1,1,2,2,2]
    # print(sol.maxEqualFreq(nums))
    # nums = [10,2,8,9,3,8,1,5,2,3,7,6]
    # print(sol.maxEqualFreq(nums))
    # nums = [1,2,3,4,5,6,7,8,9]
    # print(sol.maxEqualFreq(nums))
    nums = [1, 1]
    print(sol.maxEqualFreq(nums))
