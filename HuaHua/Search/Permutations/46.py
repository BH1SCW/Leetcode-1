from __future__ import annotations
class Solution:
    # iterative approach， 这两道题其实没啥太特别的，iterative的方式反而简单很多
    def permute(self, nums):
        ans = [[]]
        for i, n in enumerate(nums):
            ans = [a[:j] + [n] + a[j:] for a in ans for j in range(len(a) + 1)]
        return ans

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(ns, path):
            if not ns:
                ans.append(path)
            for i in range(len(ns)):
                dfs(ns[0:i] + (ns[i + 1:] if i + 1 < len(ns) else []), path + [ns[i]])
        dfs(nums, [])
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if not nums:
                return [nums]
            ans = []
            for i, n in enumerate(nums):
                ans += [[n] + i for i in helper(nums[:i] + nums[i + 1:])]
            return ans

        return helper(nums)


# ans=[] path=[] ns=[1, 2, 3]
# ans=[] path=[1] ns=[2, 3]
# ans=[] path=[1, 2] ns=[3]
# ans=[] path=[1, 2, 3] ns=[]
# ans=[] path=[1, 3] ns=[2]
# ans=[] path=[1, 3, 2] ns=[]

# ans=[] path=[2] ns=[1, 3]
# ans=[] path=[2, 1] ns=[3]
# ans=[] path=[2, 1, 3] ns=[]

# ans=[] path=[3] ns=[1, 2]

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))

