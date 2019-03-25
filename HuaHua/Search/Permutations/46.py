class Solution:
    def permute(self, nums):
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

