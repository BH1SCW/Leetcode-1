# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        for key in sorted(intervals, lambda i: i.start):
            if out and key.start <= out[-1].end:
                out[-1].end = max(key.end, out[-1].end)
            else:
                out += key
        return out