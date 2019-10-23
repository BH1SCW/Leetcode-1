class Solution:
    def permuteUnique(self, nums):
        ans = [[]]
        for i, n in enumerate(nums):
            new = []
            for a in ans:
                for j in range(len(a) + 1):
                    if j > 0 and n == a[j - 1]:
                        break
                    new += [a[:j] + [n] + a[j:]]
            ans = new
            # ans = [a[:j] + [n] + a[j:] for a in ans for j in range(len(a) + 1) if not (j > 0 and n == a[j - 1])]
        return ans

    def permuteUnique2(self, nums):
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
                # 这个小trick和combination那个一样，还没有吃透啊
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
