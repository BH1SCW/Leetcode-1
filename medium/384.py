import random
class Solution:

    def __init__(self, nums: 'List[int]'):
        self.old = nums

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        return self.old

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        new = self.old[:]
        for i in range(len(new) - 1, 0, -1):
            j = random.randint(0, i)
            new[j], new[i] = new[i], new[j]
        return new


d