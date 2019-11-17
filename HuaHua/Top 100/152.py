class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg, pos = [min(n, 0) for n in nums], [max(n, 0) for n in nums]
        ans = nums[0]
        for i, n in enumerate(nums):
            if n > 0:
                if i and pos[i - 1]: pos[i] = n * pos[i - 1]
                if i and neg[i - 1]: neg[i] = n * neg[i - 1]
                ans = max(pos[i], ans)
            elif n < 0:
                if i and neg[i - 1]: pos[i] = n * neg[i - 1]
                if i and pos[i - 1]: neg[i] = n * pos[i - 1]
                if pos[i]: ans = max(pos[i], ans)
            else:
                ans = max(n, ans)
        return ans

