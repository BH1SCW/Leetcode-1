class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.insert_table = {}
        self.random_table = {}
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.size += 1
        if val in self.insert_table:
            # add the number of duplicate values
            self.insert_table[val][0] += 1
            size = self.insert_table[val][0]
            # use hash function to remember the location
            self.insert_table[val][1][self.size] = size
            # add value to random table
            self.random_table[self.size] = val
            return True
        else:
            self.insert_table[val] = [1, {self.size:1}, {1:}]
            self.random_table[self.size] = val
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.insert_table:
            size = self.insert_table[val][0]
            location_map = self.insert_table[val][1]
            if size == 1:
                loc_delete = location_map[1]
                last_val = self.random_table[self.size]
                size_replace = self.insert_table[last_val][0]
                loc_replace = self.insert_table[last_val][1][size_replace]

                self.insert_table.pop(val, None)
                self.random_table[location] = self.random_table[self.size]
                self.size -= 1

            self.random_table[self.size] = val
            return True
        else:
            self.insert_table[val] = 1
            self.random_table[self.size] = val
            return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """

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

