class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x + 1
        while low < high - 1:
            mid = (low + high) // 2
            p = mid * mid
            if p == x:
                return mid
            if p < x:
                low = mid
            else:
                high = mid
        return low
