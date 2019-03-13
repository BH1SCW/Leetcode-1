class Solution:
    def change(self, amount: 'int', coins: 'List[int]') -> 'int':
        # ans = []
        # def helper(index, target, partial, ans):
        #     if target < 0:
        #         return
        #     if target == 0:
        #         ans.append(partial)
        #     else:
        #         for i in range(index, len(coins)):
        #             helper(i, target - coins[i], partial + [coins[i]], ans)
        # helper(0, amount, [], ans)
        # return len(ans)
        ans = [0] * (amount + 1)
        if not amount:
            return 0
        for value in coins:
            if value <= amount:
                ans[value] = 1
            else:
                continue
            for i in range(value + 1, amount + 1):
                if ans[i - value]:
                    if ans[i]:
                        ans[i] = min(ans[i], ans[i - value] + 1)
                    else:
                        ans[i] = ans[i - value] + 1
        return ans[-1] if ans[-1] else -1
# [1, 2, 5] amout = 11
#           0 1 2 3 4 5 6 7 8 9 10 11
# [5]       1 0 0 0 0 1 0 0 0 0 2  0
# [5, 2]    0 0 0 0 0 0 0 0 0 0 0  0
# dp[num_type_coin] =

# dfs(coins_used, coins, amout)
# dfs(1, [1, 2], 6)
# dfs(2, [1, 2], 1)





if __name__ == '__main__':
    sol = Solution()
    coins = []
    amount = 0
    coins = [1]
    amount = 0
    coins = [2]
    amount = 1
    coins = [1, 2, 5]
    amount = 11
    coins = [2]
    amount = 3
    print(sol.change(amount, coins))

