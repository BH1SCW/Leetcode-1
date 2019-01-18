# Merge k sorted list
# T(k) = 2T(k/2) + O(nk), n can ce seen as constant, so complexity is nklgk

# Definition for singly-linked list.
from Algorithm.Heapsort import Rand
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    n1 = l1
    n2 = l2
    if n1.val > n2.val:
        first = ListNode(n2.val)
        n2 = n2.next
    else:
        first = ListNode(n1.val)
        n1 = n1.next
    # start the first node
    tail = first
    while True:
        if n1 is None:
            tail.next = n2
            printList(first)
            return first
        if n2 is None:
            tail.next = n1
            printList(first)
            return first
        if n1.val > n2.val:
            tail.next = n2
            tail = tail.next
            n2 = n2.next
        else:
            tail.next = n1
            tail = tail.next
            n1 = n1.next

def mergeLists(lists):
    k = len(lists)
    i = 0
    j = k - 1
    result = []
    while i < j:
        newlist = merge(lists[i], lists[j])
        result.append(newlist)
        i += 1
        j -= 1
    if i == j:
        result.append(lists[i])
    return result


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return lists
        result = lists
        while len(result) > 1:
            result = mergeLists(result)
        return result[0]

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

if __name__ == '__main__':
    a1 = sorted(Rand(3))
    printList(makeList(a1))
    l1 = makeList(a1)
    a2 = sorted(Rand(3))
    l2 = makeList(a2)
    a3 = sorted(Rand(3))
    l3 = makeList(a3)
    sol = Solution()
    result = sol.mergeKLists([l1, l2, l3])
    printList(result)

