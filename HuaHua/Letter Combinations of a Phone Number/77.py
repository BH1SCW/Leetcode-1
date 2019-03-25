class Solution:
    def combine(self, n: int, k: int) -> 'List[List[int]]':
        nums = list(range(1, n + 1))
        ans = []
        for n in nums:
            ans.append([n])
        for ke in range(1, k):
            new = []
            for ne in nums:
                for ae in ans:
                    if ne > ae[-1]:
                        new.append(ae + [ne])
            ans = new
        return ans

if __name__ == '__main__':
    sol = Solution()
    n, k = 4, 2
    print(sol.combine(n, k))

