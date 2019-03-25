class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        def dfs(ns, path):
            if not ns:
                ans.append(path)
            for i in range(len(ns)):
                if i > 0 and ns[i] == ns[i - 1]:
                    continue
                dfs(ns[0:i] + (ns[i + 1:] if i + 1 < len(ns) else []), path + [ns[i]])
        dfs(nums, [])
        return ans

# ans=[] path=[] ns=[1, 2, 2]
# ans=[] path=[1] ns=[2, 2]
    # ans=[] path=[1, 2] ns=[2]
        # ans=[] path=[1, 1, 2] ns=[2]
            # ans=[] path=[1, 1, 2, 2] ns=[]
# ans=[] path=[2] ns=[1, 2]

# ans=[] path=[1, 2] ns=[2]
# ans=[] path=[1, 2, 2] ns=[]

# ans=[] path=[1, 2, 3] ns=[]
# ans=[] path=[1, 3] ns=[2]
# ans=[] path=[1, 3, 2] ns=[]



if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2]
    print(sol.permuteUnique(nums))
