from collections import defaultdict
class Solution:
    # 这题的解法确实很多。。有一个voting的算法确实很有趣
    def majorityElement(self, nums: List[int]) -> int:
        f, maxF, maj = defaultdict(int), 0, 0
        for n in nums:
            f[n] += 1
            if f[n] > maxF:
                maxF, maj = f[n], n
                if maxF > len(nums) // 2:
                    return maj



