from __future__ import annotations
class Solution:
    # 参考：https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            i = res = 0
            for j, n in enumerate(nums):
                k -= n % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1
            return res
        return at_most(k) - at_most(k - 1)

    # 我这个做法也是相当不错的，不过看了一下别人的解法还是更牛逼，这个跟上次做的一道sliding window很像
    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        index = []
        for i, n in enumerate(nums):
            if n % 2:
                index.append(i)
        ans = 0
        for i, ind in enumerate(index):
            if i + k - 1 > len(index) - 1:
                break
            j = index[i + k - 1]
            s = index[i - 1] + 1 if i else 0
            e = index[i + k] - 1 if i + k < len(index) else len(nums) - 1
            ans += (ind - s + 1) * (e - j + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    print(sol.numberOfSubarrays(nums, k))
