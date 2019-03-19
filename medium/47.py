class Solution:
    def permute(self, nums):
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
                dfs(ns[0:i] + (ns[i + 1:] if i + 1 < len(ns) else []), path + [ns[i]])
        dfs(nums, [])
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))
