class Solution:
    def longestConsecutive(self, nums):
        numbers = set(nums)
        found = set()
        ans = 0
        for n in nums:
            if n in found:
                continue
            k = n
            count = 1
            found.add(k)
            while k - 1 in numbers:
                count += 1
                k -= 1
                found.add(k) # actually add k - 1
            k = n
            while k + 1 in numbers:
                count += 1
                k += 1
                found.add(k) # actually k + 1
            ans = max(ans, count)
        return ans

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))

