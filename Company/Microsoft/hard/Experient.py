def test(s):
    s[0] = 2

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def test2(n):
    n = ListNode(3)

def test3(n):
    n.val = 3

def test4(n):
    l = n
    print("test4 is {}".format(l.next.val))


if __name__ == '__main__':
    s = [1]
    test(s)
    print(s)
    s = 10
    while s > 0:
        s -= 1
    print(s)
    n = ListNode(4)
    n.next = ListNode(5)
    test2(n)
    print("test2 is {}".format(n.val))
    test3(n)
    print("test3 is {}".format(n.val))
    test4(n)
