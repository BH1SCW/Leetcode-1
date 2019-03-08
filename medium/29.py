class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = 1 if (divisor > 0) is (dividend > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        temp = divisor
        target = dividend
        i = 0
        while temp < dividend:
            temp <<= 1
            i += 1
        while i >= 0:
            if temp == target:
                ans += 2 ** i
                break
            if temp < target:
                ans += 2 ** i
                target -= temp
            temp >>= 1
            i -= 1
        return positive *  ans

        # def helper(dividend, divisor, i):
        #     global ans
        #     if dividend > divisor:
        #         ans += 2 ^ i
        #     else:
        #         helper(dividend, divisor >> 1, i - 1)

if __name__ == '__main__':
    sol = Solution()
    s = 10
    t = 3
    # s = 7
    # t = -3
    print(sol.divide(s, t))
