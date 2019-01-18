# Merge k sorted list
# T(k) = 2T(k/2) + O(nk), n can ce seen as constant, so complexity is nklgk

# Definition for singly-linked list.
from Algorithm.Heapsort import Rand
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def makeList(s):
    s1 = ListNode(s[0])
    head = s1
    for i in range(1, len(s)):
        s1.next = ListNode(s[i])
        s1 = s1.next
    return head

def printList(s):
    s1 = ""
    while not (s is None):
        s1 += str(s.val)
        s1+= " "
        s = s.next
    print(s1)

class MinHeap():
    def __init__(self, s):
        self.size = len(s)
        self.heap = s
        for i in range(self.size - 1, -1, -1):
            if self.heap[i] is None:
                self.heap[i] = ListNode(math.inf)
            self.minHeapify(i)

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if i <= self.size - 1:
            minimum = i
            if l < self.size and self.heap[l].val <= self.heap[i].val:
                minimum = l
            if r < self.size and self.heap[r].val <= self.heap[minimum].val:
                minimum = r
            if minimum != i:
                self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
                self.minHeapify(minimum)

    def extractMin(self):
        if self.size >= 1:
            head = self.heap[0]
            if not (head.next is None):
                self.heap[0] = head.next
            else:
                self.heap[0] = ListNode(math.inf)
            self.minHeapify(0)
            return head

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return lists
        list = []
        heap = MinHeap(lists)
        result = heap.extractMin()
        if result.val < math.inf:
            first = result
            tail = first
            while True:
                result = heap.extractMin()
                if result.val < math.inf:
                    tail.next = result
                    tail = tail.next
                else:
                    tail.next = None
                    return first
        else:
            return []




if __name__ == '__main__':
    a1 = sorted(Rand(3))
    l1 = makeList(a1)
    a2 = sorted(Rand(3))
    l2 = makeList(a2)
    a3 = sorted(Rand(3))
    l3 = makeList(a3)
    # heap = MinHeap([l1, l2, l3])

    # s = ""
    # while True:
    #     result = heap.extractMin()
    #     if result.val < math.inf:
    #         s += str(result.val)
    #         s += " "
    #     else:
    #         break
    # print(s)
    #
    sol = Solution()
    # printList(sol.mergeKLists([l1, l2, l3]))
    printList(sol.mergeKLists([[]]))

