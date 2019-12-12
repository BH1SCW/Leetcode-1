def deepCopy(head):
    # WRITE YOUR CODE HERE
    prev = dummy = ALNode(0)
    dic = {}
    while head:
        dic[head] = prev.next = cur = ALNode(head.value)
        cur.arbitrary = head
        prev = cur
        head = head.next
    cur = dummy.next
    while cur:
        cur.arbitrary = dic[cur.arbitrary.arbitrary]
        cur = cur.next
    return dummy.next

