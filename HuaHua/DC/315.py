from collections import defaultdict, deque
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count = [0] * len(nums)
        def helper(i, j):
            if i == j:
                return deque([(nums[i], i)])
            else:
                q = deque([(1, 1)] * (j - i + 1))
                m = (i + j) // 2
                l = helper(i, m)
                r = helper(m + 1, j)
                for _ in range(i, j + 1):
                    if not r or l and l[-1][0] > r[-1][0]:
                        count[l[-1][1]] += len(r)
                        item = l.pop(-1)
                    else:
                        item = r.pop(-1)
                    q.appendleft(item)
        helper(0, len(nums) - 1)
        return count

    # 这个理论上是O(nlgn)，居然超时了。
    def countSmaller2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count = [0] * len(nums)
        def helper(i, j):
            d, min_e, max_e = defaultdict(int), 0, 0
            if i == j:
                d[nums[i]], min_e, max_e = 1, nums[i], nums[i]
            else:
                m = (i + j) // 2
                d1, min_e1, max_e1 = helper(i, m)
                d2, min_e2, max_e2 = helper(m + 1, j)
                min_e, max_e = min(min_e1, min_e2), max(max_e1, max_e2)
                for k in range(min_e, max_e + 1):
                    d1[k] = max(d1[k], d1[k - 1])
                    d2[k] = max(d2[k], d2[k - 1])
                    d[k] = d1[k] + d2[k]
                for k in range(i, m + 1):
                    count[k] += d2[nums[k] - 1]
            return d, min_e, max_e
        helper(0, len(nums) - 1)
        return count


