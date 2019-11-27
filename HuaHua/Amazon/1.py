class SLNode:
    def __init__(self, key):
        self.val = key
        self.next = None

def mergeLists(head1, head2):
    # WRITE YOUR CODE HERE
    cur = dummy = SLNode(0)
    while head1 or head2:
        if not head2 or (head1 and head1.val <= head2.val):
            cur.next = SLNode(head1.val)
            head1 = head1.next
        else:
            cur.next = SLNode(head2.val)
            head2 = head2.next
        cur = cur.next
    return dummy.next

if __name__ == '__main__':
    h1 = head1 = SLNode(1)
    head1.next = SLNode(2)
    head1 = head1.next
    head1.next = SLNode(3)
    head1 = head1.next
    head1.next = SLNode(4)
    head1 = head1.next
    h2 = head2 = SLNode(1)
    head2.next = SLNode(3)
    head2 = head2.next
    head2.next = SLNode(5)
    head2 = head2.next
    head2.next = SLNode(7)
    head2 = head2.next
    print(mergeLists(h1, h2))
