class Solution:
    def sort(self, row):
        """counting sort the row"""
        n = len(row) / 2 # the number of the couple
        c = [0 for i in range(n)]
        [c[reprow[i * 2]] = 1 for i in range(n)]

    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """


