import random
class RandomizedCollection:
    def __init__(self):
        self.array = [] # (val, index of prev same val)
        self.hash = {} # (val, array_index)
        self.size = 0

    def insert(self, val):
        if val in self.hash:
            # self.array[self.size] = (val, self.hash[val])
            self.array.append((val, self.hash[val]))
            self.hash[val] = self.size
            self.size += 1
            return False
        else:
            # self.array[self.size] = (val, -1)
            self.array.append((val, -1))
            self.hash[val] = self.size
            self.size += 1
            return True

    def remove(self, val):
        if val in self.hash:
            index  = self.hash[val]
            node = self.array[index]
            last_node = self.array[self.size - 1]
            last_val = last_node[0]
            # this is no repetitious element
            if node[1] == -1:
                # this means we are removing the last element, there is no hole
                if last_node == node:
                    # delete hash table entry
                    self.hash.pop(val, None)
                    # self.array[self.size - 1] = ()
                else:
                    # change the hash table entry
                    self.hash[last_val] = index
                    # change the array
                    self.array[index] = last_node
                    # delete hash table entry
                    self.hash.pop(val, None)
                    # self.array[self.size - 1] = ()
                    # self.size -= 1
            else:
                if last_node == node:
                    self.hash[last_val] = node[1]
                    # delete hash table entry
                    # self.array[self.size - 1] = ()
                    # self.size -= 1
                else:
                    if node[1] == self.size - 1:
                        self.hash[last_val] = index
                        self.array[index] = last_node
                    else:
                        # change the hash table entry
                        self.hash[last_val] = index
                        self.hash[val] = node[1]
                        # change the array
                        self.array[index] = last_node
                        # self.array[self.size - 1] = ()
                        # self.size -= 1
            self.array.pop()
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self):
        return self.array[random.randint(0, self.size - 1)][0]

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
            print(ran.hash)
            print(ran.array)
            ran.insert(val)
            print("After insert {}".format(val))
            print(ran.hash)
            print(ran.array)
            print('-' * 30)
        if com == "remove":
            print("Before remove {}".format(val))
            print(ran.hash)
            print(ran.array)
            ran.remove(val)
            print("After remove {}".format(val))
            print(ran.hash)
            print(ran.array)
            print('-' * 30)
                # print("-" * 30)
                # print("ERROR")
                #
