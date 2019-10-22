# 这道题虽然我以前过了，但是其实没有想通
from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = defaultdict(int)
        ans[0] = 1
        for coin in coins:
            for target in range(coin, amount + 1):
                ans[target] += ans[target - coin]
        return ans[amount]

