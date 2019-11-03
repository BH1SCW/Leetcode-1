from __future__ import annotations
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = {}
        stack = []
        i, N = 0, len(nums)
        while nums:
            n = nums[i % N]
            if len(ans) == N or stack and i - N >= stack[-1]:
                break
            while stack and nums[stack[-1]] < n:
                ans[stack.pop()] = n
            if not i % N in ans:
                stack += [i % N]
            i += 1
        return [ans.get(i, -1) for i, n1 in enumerate(nums)]


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,1]
    print(sol.nextGreaterElements(nums))
    nums = []
    print(sol.nextGreaterElements(nums))
    nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    print(sol.nextGreaterElements(nums))
