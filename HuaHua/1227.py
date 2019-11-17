from __future__ import annotations
import itertools
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        ans = count = 0
        for p in itertools.permutations(range(n)):
            count += 1
            if p[-1] ==


