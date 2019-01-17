# Merge Sort
# T(n) = 2T(n/2) + n
# According to Master's Theory, T(n) = aT(n/b) + f(n), log_b(a) = 1
import random

def Merge(s1, s2):
    """Merge two sorted list together
    Input:
    s1 = [1, 3]
    s2 = [2, 4]
    Output:
    [1, 2, 3, 4]
    """
    s = []
    i = 0
    j = 0
    while i <= len(s1) - 1 or j <= len(s2) - 1:
        # Important: only one action is taken, continue is vital here, otherwise index could be out of range.
        if j >= len(s2):
            s.append(s1[i])
            i += 1
            continue
        if i >= len(s1):
            s.append(s2[j])
            j += 1
            continue
        if s1[i] <= s2[j]:
            s.append(s1[i])
            i += 1
        else:
            s.append(s2[j])
            j += 1
    return s

def MergeSort(s):
    # corner case
    if len(s) == 0:
        return s
    # base case
    if len(s) == 1:
        return s
    else:
        mid = len(s) // 2
        s1 = MergeSort(s[0 : mid])
        s2 = MergeSort(s[mid : ])
        s3 = Merge(s1, s2)
        return s3


def Rand(num, start=0, end=100):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res

if __name__ == "__main__":
    s1 = [1]
    s2 = [2]
    print(Merge(s1, s2))
    # corner case
    s = [1]
    print(s)
    print(MergeSort(s))
    s = [1, 3]
    print(s)
    print(MergeSort(s))
    s = [3, 1]
    print(s)
    print(MergeSort(s))
    s = [1, 5, 4]
    print(s)
    print(MergeSort(s))
    s = Rand(10)
    print(s)
    print(MergeSort(s))
    s = Rand(30)
    print(s)
    print(MergeSort(s))
