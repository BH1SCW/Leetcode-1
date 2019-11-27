from __future__ import annotations
class Solution:
    # 这题居然是greedy的，真的看不出来
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        s = [gas[i] - cost[i] for i in range(N)]
        for i in range(1, N):
            s[i] += s[i - 1]
        return s.index(min(s))
    
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        pre, nxt, nxt_sum, pre_sum = [0] * (N + 2), [0] * (N + 2), [0] * (N + 2), [0] * (N + 2)
        diff = [0] + [gas[i] - cost[i] for i in range(N)] + [0]
        for i in range(1, N + 1)[::-1]:
            nxt[i] = max(nxt[i + 1] - diff[i], 0)
            # if diff[i] >= nxt[i + 1]:
            #     nxt[i] = 0
            # else:
            #     nxt[i] = nxt[i + 1] - diff[i]
            nxt_sum[i] = diff[i] + nxt_sum[i + 1]
        for i in range(1, N + 1):
            left = pre_sum[i - 1] + pre[i - 1]
            pre[i] = pre[i - 1] - min(left + diff[i], 0)
            # if left + diff[i] >= 0:
            #     pre[i] = pre[i - 1]
            # else:
            #     pre[i] = pre[i - 1] - (left + diff[i])
            pre_sum[i] = diff[i] + pre_sum[i - 1]
        for i in range(1, N + 1):
            if diff[i] < 0: continue
            if nxt[i] == 0 and nxt_sum[i] >= pre[i - 1]: return i - 1
        return -1

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     N = len(gas)
    #     for i, g in enumerate(gas):
    #         s, left = i, 0
    #         for d in range(N):
    #             s = (i + d) % N
    #             left += (gas[s] - cost[s])
    #             if left <= 0: break
    #         if d == N - 1 and left >= 0: return i
    #     return -1

if __name__ == '__main__':
    sol = Solution()
    # gas = [4, 5, 2, 6, 5, 3]
    # cost = [3, 2, 7, 3, 2, 9]
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    print(sol.canCompleteCircuit(gas, cost))
