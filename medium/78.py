class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new = []
            for a in ans:
                new.append(a + [n])
            ans += new
        return ans
