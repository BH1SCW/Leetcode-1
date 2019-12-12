import collections
class Solution:
    def isPossible(self, nums):
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2, 3]
    print(sol.isPossible(nums))
