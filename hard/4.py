# Divide and Conquer
# [0 1 2 3 4 5 6 7] m = 8
# [5 7 9 11 13 6] n = 6
from Algorithm.Heapsort import Rand
from Algorithm.QuickSort import QuickSort
# important: this still cannot handle empty list, but this is good enough
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        global i, j, median
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        lb = 0
        ub = m
        median = 0
        if m != 0 and n != 0:
            while lb <= ub:
                # m = 8, n = 7, k = 8
                i = (lb + ub) // 2 # i = 3
                j = (n + m + 1) // 2 - i # j = 4
                if i <= m - 1 and j >= 1 and nums2[j - 1] > nums1[i]:
                    lb = i + 1
                    continue
                if i >= 1 and j <= n - 1 and nums1[i - 1] > nums2[j]:
                    ub = i - 1
                    continue
                median = max(nums1[i - 1], nums2[j - 1])
                break
            if (n + m) % 2 == 1:
                return median
            if i == m:
                return (median + nums2[j]) / 2.0
            if j == n:
                return (median + nums1[i]) / 2.0
            return (median + min(nums1[i], nums2[j])) / 2.0
        if m == 0:
            return med(nums2)
        if n == 0:
            return med(nums1)

def med(l):
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return l[len(l) // 2] + l[len(l) // 2 - 1]


if __name__ == '__main__':
    sol = Solution()
    s1 = Rand(10)
    s2 = Rand(20)
    QuickSort(s1, 0, 9)
    QuickSort(s2, 0, 19)
    s1 = [1, 3]
    s2 = [2]
    s1 = [2]
    s2 = []
    s1 = []
    s2 = [2]
    s1= [1]
    s2 = [2, 3, 4]
    print(sol.findMedianSortedArrays(s1, s2))




