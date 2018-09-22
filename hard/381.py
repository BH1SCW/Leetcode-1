import random
class Node:
    def __init__(self, val, prv, nxt):
        self.val = val
        self.nxt = nxt
        self.prv = prv

class RandomizedCollection:
    def __init__(self):
        self.array = [] # (val, index of prev same val)
        self.hash = {} # (val, array_index)
        self.size = 0

    def insert(self, val):
        if val in self.hash:
            self.array.append(Node(val, self.hash[val], None))
            prv_node = self.array[self.hash[val]]
            prv_node.nxt = self.size
            self.hash[val] = self.size
            self.size += 1
            return False
        else:
            # self.array[self.size] = (val, -1)
            self.array.append(Node(val, None, None))
            self.hash[val] = self.size
            self.size += 1
            return True

    def remove(self, val):
        if val in self.hash:
            index = self.hash[val]
            node = self.array[index]
            last_node = self.array[self.size - 1]
            last_val = last_node.val
            # this is no repetitious element
            if node.prv == None:
                # this means we are removing the last element, there is no hole
                if last_node != node:
                    if last_node.nxt == None:
                        # change the hash table entry
                        self.hash[last_val] = index
                    else:
                        nxt_node = self.array[last_node.nxt]
                        nxt_node.prv = index
                        if last_node.prv != None:
                            prv_node = self.array[last_node.prv]
                            prv_node.nxt = index
                    # change the array
                    self.array[index] = last_node
                # delete hash table entry
                self.hash.pop(val, None)
            else:
                self.hash[val] = node.prv
                self.array[node.prv].nxt = None
                if last_node == node:
                    self.hash[last_val] = node.prv
                else:
                    if node.prv == self.size - 1:
                        self.hash[last_val] = index
                    else:
                        if last_node.nxt == None:
                            # change the hash table entry
                            self.hash[last_val] = index
                        else:
                            nxt_node = self.array[last_node.nxt]
                            nxt_node.prv = index
                    # change the array
                    self.array[index] = last_node
                    if last_node.prv != None:
                        prv_node = self.array[last_node.prv]
                        prv_node.nxt = index
            self.array.pop()
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self):
        return self.array[random.randint(0, self.size - 1)].val

    def print(self):
        print(self.hash)
        s = ''
        for i in range(self.size):
            n = self.array[i]
            # s += '{}: (val:{}, nxt:{}) '.format(i, n.val, n.nxt)
            s += '{}: (val:{}, nxt:{}, prv:{}) '.format(i, n.val, n.nxt, n.prv)
        print(s)

if __name__ == "__main__":
    ran = RandomizedCollection()
    command = ["RandomizedCollection","insert","insert","insert","insert","insert","insert","remove","remove","remove","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
    vals = [[],[1],[1],[2],[1],[2],[2],[1],[2],[2],[2],[],[],[],[],[],[],[],[],[],[]]
    command = ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
    vals = [[], [1], [1], [2], [], [1], []]
    command = ["RandomizedCollection", "insert", "insert", "insert", "insert", "insert", "insert", "remove", "remove", "remove",
     "remove", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom",
     "getRandom", "getRandom"]
    vals = [[], [10], [10], [20], [20], [30], [30], [10], [10], [30], [30], [], [], [], [], [], [], [], [], [], []]
    for i in range(1, len(vals)):
        com = command[i]
        val = vals[i]
        if len(val) != 0:
            val = val[0]
        if com == "insert":
            # if val[0] == 13:
                #print("Error here.")
            print("Before insert {}".format(val))
            ran.print()
            ran.insert(val)
            print("After insert {}".format(val))
            ran.print()
            print('-' * 30)
        if com == "remove":
            print("Before remove {}".format(val))
            ran.print()
            ran.remove(val)
            print("After remove {}".format(val))
            ran.print()
            print('-' * 30)
                # print("-" * 30)
                # print("ERROR")
                #
