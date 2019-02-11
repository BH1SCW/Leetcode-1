import functools
class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        compare = lambda x, y: 1 if x + y > y + x else -1
        ns = list(map(str, nums))
        ns.sort(key=functools.cmp_to_key(compare), reverse=True)
        return str(int(''.join(ns)))




if __name__ == '__main__':
    nums = [10, 2]
    nums = [3,30,34,5,9]
    sol = Solution()
    print(sol.largestNumber(nums))

