class Solution:
    # 这道题看起来简单，但是还是有着很多的小细节的，比如说同一元素不能够重复用，所以要先检查，后加入字典
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]
            d[nums[i]] = i
        # return [d.pop(n) or [i, d[target - n]] for (i, n) in zip(range(len(nums)), nums) if target - n in d]

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     d = {}
    #     for i in range(len(nums)):
    #         d[nums[i]] = i
    #     return [d.pop(n) or [i, d[target - n]] for (i, n) in zip(range(len(nums)), nums) if target - n in d]
    #

