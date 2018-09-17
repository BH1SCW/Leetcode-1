class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash_table = {}
        self.linked_list = linked_list()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_table:
            node = self.hash_table[key][1]
            val = self.hash_table[key][0]
            #print("Before Get {}:".format(key))
            # self.linked_list.print()
            self.linked_list.move(node)
            #print("After Get {}:".format(key))
            # self.linked_list.print()
            #print(self.hash_table)
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # add key value only when the key doesn't exist
        if not key in self.hash_table:
            # if size exceeds capacity, remove the end of list
            if self.linked_list.size >= self.capacity:
                #print("Before add {}:".format(key))
                # self.linked_list.print()
                end = self.linked_list.delete()
                node = self.linked_list.add(key)
                # hash table stores value and node address
                self.hash_table[key] = (value, node)
                #print("just add {}".format(key))
                #print("After add {}:".format(key))
                # self.linked_list.print()
                self.hash_table.pop(end, None)
                #print(self.hash_table)
            else:
                #print("Before add {}:".format(key))
                # self.linked_list.print()
                node = self.linked_list.add(key)
                #print("just add {}".format(key))
                #print("After add {}:".format(key))
                # self.linked_list.print()
                self.hash_table[key] = (value, node)
        else:
            # update the value when key is present
            #print("Before put {}:".format(key))
            # self.linked_list.print()
            node = self.hash_table[key][1]
            self.hash_table[key] = (value, node)
            self.linked_list.move(node)
            #print("After put {}:".format(key))
            # self.linked_list.print()

class Node:
    def __init__(self, val, nxt, prv):
        self.val = val
        self.nxt = nxt
        self.prv = prv

class linked_list:
    def __init__(self, val):
        self.head = Node(val, self.end, None)
        self.end = self.head
        self.size = 1

    def __init__(self):
        self.size = 0

    def move(self, node):
        if node == self.head:
            return node
        # if node == self.end:
        else:
            prv = node.prv
            nxt = node.nxt
            prv.nxt = nxt
            if nxt != None:
                nxt.prv = prv
            else:
                self.end = prv
            node.nxt = self.head
            node.prv = None
            self.head.prv = node
            self.head = node
            return node

    def add(self, val):
        if self.size == 0:
            self.head = Node(val, None, None)
            self.end = self.head
            self.size += 1
            return self.head
        else:
            # always add to the head
            head = Node(val, self.head, None)
            self.head.prv = head
            if self.size == 1:
                self.end = self.head
            self.head = head
            self.size += 1
            return head

    def delete(self):
        self.size -= 1
        end = self.end
        end.nxt = None
        prv = end.prv
        if prv != None:
            prv.nxt = None
        end.prv = None
        key = end.val
        self.end = prv
        return key

    def print(self):
        print("linked list size {}".format(self.size))
        if self.size != 0:
            node = self.head
            s = ""
            while node != None:
                s += "{} ->".format(node.val)
                node = node.nxt
            print(s)

if __name__ == "__main__":
    command = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    vals = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    command = ["LRUCache", "put", "put", "put", "put", "get", "get"]
    vals = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    command = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    vals = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
    out = ["null", "null", "null", "null", "null", "null", -1, "null", 19, 17, "null", -1, "null", "null", "null", -1, "null", -1, 5, -1, 12, "null",
     "null", 3, 5, 5, "null", "null", 1, "null", -1, "null", 30, 5, 30, "null", "null", "null", -1, "null", -1, 24, "null", "null", 18, "null",
     "null", "null", "null", -1, "null", "null", 18, "null", "null", -1, "null", "null", "null", "null", "null", 18, "null", "null", -1, "null", 4,
     29, 30, "null", 12, -1, "null", "null", "null", "null", 29, "null", "null", "null", "null", 17, 22, 18, "null", "null", "null", -1, "null",
     "null", "null", 20, "null", "null", "null", -1, 18, 18, "null", "null", "null", "null", 20, "null", "null", "null", "null", "null", "null", "null"]
    lru = LRUCache(vals[0][0])
    for i in range(len(vals)):
        com = command[i]
        val = vals[i]
        if com == "put":
            # if val[0] == 13:
                #print("Error here.")
            lru.put(val[0], val[1])
        if com == "get":
            o = lru.get(val[0])
            answer = out[i]
            if o != answer:
                print("-" * 30)
                print("ERROR")
                #print(lru.hash_table)
