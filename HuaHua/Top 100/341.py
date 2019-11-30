class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList
        self.iter = self.list[0]
        self.i = 0
        self.N = 0

    def next(self):
        """
        :rtype: int
        """
        if self.iter.isInteger():
            self.i += 1
            self.iter = self.list[i] if i < self.N else None
            return self.


    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.iter is None