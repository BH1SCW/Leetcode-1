from __future__ import annotations


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n:
            s += n % 10
            p *= n % 10
            n //= 10
        return p - s



if __name__ == '__main__':
    sol = Solution()
    n = 9
    print(sol.subtractProductAndSum(n))
    n = 1
    print(sol.subtractProductAndSum(n))
    n = 10
    print(sol.subtractProductAndSum(n))
    n = 123
    print(sol.subtractProductAndSum(n))
    n = 234
    print(sol.subtractProductAndSum(n))
    n = 4421
    print(sol.subtractProductAndSum(n))
