from __future__ import annotations
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                ans[stack.pop()] = n
            stack += [n]
        return [ans.get(n1, -1) for n1 in nums1]



if __name__ == '__main__':
    sol = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(sol.nextGreaterElement(nums1, nums2))
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(sol.nextGreaterElement(nums1, nums2))
