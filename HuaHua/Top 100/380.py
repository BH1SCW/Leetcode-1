from __future__ import annotations
from random import randrange
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        nums, pos = self.nums, self.pos
        if val in pos: return False
        nums.append(val)
        pos[val] = len(nums) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        nums, pos = self.nums, self.pos
        if not val in pos: return False
        val_pos, last = pos[val], nums.pop()
        del pos[val]
        if val_pos < len(nums):
            pos[last] = val_pos
            nums[val_pos] = last
        return True



    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[randrange(len(self.nums))]

