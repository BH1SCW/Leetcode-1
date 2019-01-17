# quicksort is a very good sorting algorithm in practice, it has the advantage of in-place sorting.
# however, the performance depends on the partition
# if the array has already been sorted, then T(n) = T(n- 1) + T(0) + O(n)
# if the arrya was equally partitioned, then T(n) = 2T(n / 2) + O(n)
# Important: Supprisingly, quick sort is the simplest to implement. There is almost no problem when implementing.
from Algorithm.Heapsort import Rand
def QuickSort(s, p, q):
    if q > p:
        m = Partition(s, p, q)
        QuickSort(s, p, m - 1)
        QuickSort(s, m + 1, q)

def Partition(s, p, q):
    i = p - 1
    j = p
    while j <= q - 1:
        if s[j] < s[q]:
            i += 1
            s[j], s[i] = s[i], s[j]
        j += 1
    i += 1
    s[q], s[i] = s[i], s[q]
    return i

if __name__ == '__main__':
    s = [3, 1, 4]
    Partition(s, 0, 2)
    QuickSort(s, 0, 2)
    print(s)
    s = Rand(10)
    QuickSort(s, 0, 9)
    print(s)
    s = Rand(30)
    QuickSort(s, 0, 29)
    print(s)

