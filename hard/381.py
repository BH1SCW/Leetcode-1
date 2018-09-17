import random
class Node:
    def __init__(self, size):
        self.number = 1
        self.location = {1:size}
        self.order = {size:1}

    # def remove(self):
    #     self.

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
            # add the size of duplicate values
            self.insert_table[val][0] += 1
            size = self.insert_table[val][0]
            # use hash function to remember the location
            self.insert_table[val][1][size] = self.size
            self.insert_table[val][2][self.size] = size
            # add value to random table
            self.random_table[self.size] = val
            return False
        else:
            # self.insert_table[val] = {number:1, location:{1:self.size}, order:{self.size:1}}
            self.insert_table[val] = [1, {1:self.size}, {self.size:1}]
            self.random_table[self.size] = val
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.insert_table:
            size_remove = self.insert_table[val][0]
            location_map = self.insert_table[val][1]
            last_val = self.random_table[self.size]
            if last_val == val:
                ord_remove = self.insert_table[val][2][self.size]
                self.insert_table[val][2].pop(self.size, None)
                location_map.pop(ord_remove, None)
                self.random_table.pop(self.size, None)
                self.size -= 1
            else:
                if size_remove == 1:
                    loc_remove = location_map[1]
                    map_replace = self.insert_table[last_val][2]
                    ord_replace = map_replace[self.size]
                    self.insert_table[last_val][1][ord_replace] = loc_remove
                    map_replace.pop(self.size, None)
                    map_replace[loc_remove] = ord_replace

                    self.insert_table.pop(val, None)

                    self.random_table[loc_remove] = self.random_table[self.size]
                    self.random_table.pop(self.size, None)
                    self.size -= 1
                else:
                    loc_remove = location_map[size_remove]
                    map_replace = self.insert_table[last_val][2]
                    ord_replace = map_replace[self.size]
                    self.insert_table[last_val][1][ord_replace] = loc_remove
                    map_replace.pop(self.size, None)
                    print(self.insert_table[last_val][1])
                    print(self.insert_table[last_val][2])
                    map_replace[loc_remove] = ord_replace

                    self.insert_table[val][0] -= 1
                    self.insert_table[val][1].pop(size_remove, None)
                    self.insert_table[val][2].pop(loc_remove, None)

                    self.random_table[loc_remove] = self.random_table[self.size]
                    self.random_table.pop(self.size, None)
                    self.size -= 1
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.random_table[random.randint(1, self.size)]

if __name__ == "__main__":
    ran = RandomizedCollection()
    command = ["RandomizedCollection","insert","insert","insert","insert","insert","insert","remove","remove","remove","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
    vals = [[],[1],[1],[2],[1],[2],[2],[1],[2],[2],[2],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1, len(vals)):
        com = command[i]
        val = vals[i][0]
        if com == "insert":
            # if val[0] == 13:
                #print("Error here.")
            ran.insert(val)
            print(ran.insert_table)
            print(ran.random_table)
        if com == "remove":
            ran.remove(val)
            print(ran.insert_table)
            print(ran.random_table)
                # print("-" * 30)
                # print("ERROR")
                #
