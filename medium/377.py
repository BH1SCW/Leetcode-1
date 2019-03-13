class Solution:
    def combinationSum4(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        ans = [0] * (target + 1)
        ans[0] = 1
        for t in range(1, target + 1):
            for n in nums:
                ans[t] += ans[t - n]
        return ans[-1]
#       0 1 2 3 4
#       1 0 0 0 0
#t=1    1 1 0 0 0     1
#t=2    1 1 2 0 0     1+1 2
#t=3    1 1 2 4 0     1+(1+1) 1+2 2+1 3
#t=4    1 1 2 4 7     1+(1+(1+1)) 1+(2+1) 1+(2+1) 1+3 2+(1+1) 2+2 3+1


if __name__ == '__main__':
    sol = Solution()
    coins = [1, 2, 5]
    amount = 5
    coins = []
    amount = 0
    coins = [1]
    amount = 0
    coins = [2]
    amount = 1
    coins = [1, 2, 3]
    amount = 4
    print(sol.combinationSum4(coins, amount))

