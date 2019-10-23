from __future__ import annotations
import math
class Solution:
    # 这题虽然我想了很久，但是感觉没什么价值，这个太专门了，没什么意义
    def find132pattern(self, nums: List[int]) -> bool:
        s2 = -math.inf
        stack = []
        for n in nums[::-1]:
            if n < s2:
                return True
            else:
                while stack and n > stack[-1]:
                    s2 = stack.pop()
            stack.append(n)
        return False

