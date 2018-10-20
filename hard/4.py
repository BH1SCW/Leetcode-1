#st  [0 1 2 3 4 5 6 7]
# [5 7 9 11 13 6]
# [0 1 2 3 4 5 6 7]
# [5 7 9 11 13 6]
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)
        if len(nums1) >= len(nums2):
            return med(nums1, nums2)
        else:
            return med(nums2, nums1)

def median(l):
    lth = len(l)
    try:
        if lth % 2 == 0:
            return (l[lth // 2] + l[lth // 2 - 1]) / 2.0
        else:
            return (l[(lth - 1) // 2])
    except:
        print(l)

def med(l1, l2):
    lth1 = len(l1)
    lth2 = len(l2)
    assert len(l1) >= len(l2)
    cut = (lth2 - 1) // 2
    if lth2 == 1:
        if lth1 == 1:
            return (l1[0] + l2[0]) / 2.0
        if lth1 == 2:
            if l2[0] <= l1[0]:
                return l1[0]
            if l2[0] >= l1[1]:
                return  l1[1]
            return l2[0]
        if lth1 % 2 == 0:
            if l2[0] >= l1[lth1 // 2]:
                return l1[lth1 // 2]
            if l2[0] <= l1[lth1 // 2 - 1]:
                return l1[lth1// 2 - 1]
            return l2[0]
        else:
            if l2[0] >= l1[(lth1 - 1) // 2 + 1]:
                return (l1[(lth1 - 1) // 2] + l1[(lth1 - 1) // 2 + 1]) / 2.0
            if l2[0] <= l1[(lth1 - 1) // 2 - 1]:
                return (l1[(lth1 - 1) // 2] + l1[(lth1 - 1) // 2 - 1]) / 2.0
            return (l1[(lth1 - 1) // 2] + l2[0]) / 2.0
    if lth2 == 2:
        if lth1 == 2:
            return (max(l1[0], l2[0]) + min(l1[1], l2[1])) / 2.0
        if lth1 % 2 == 0:
            if min(l2) >= l1[lth1 // 2 + 1]:
                return (l1[lth1 // 2] + l1[lth1 // 2 + 1]) / 2.0
            if max(l2) <= l1[lth1 // 2 - 2]:
                return (l1[lth1 // 2 - 1] + l1[lth1 // 2 - 2]) / 2.0
            return med([l1[lth1 // 2 - 1], l1[lth1 // 2]], l2)
        else:
            if min(l2) >= l1[(lth1 - 1) // 2]:
                return min(min(l2), l1[(lth1 - 1) // 2 + 1])
            if max(l2) <= l1[(lth1 - 1) // 2]:
                return max(max(l2), l1[(lth1 - 1) // 2 - 1])
            return l1[(lth1 - 1) // 2]
    med1 = median(l1)
    med2 = median(l2)
    if med1 == med2:
        return med1
    if med1 > med2:
        return med(l1[0 : lth1 - cut], l2[cut : ])
    else:
        return med(l1[cut : ], l2[0 : lth2 - cut])

