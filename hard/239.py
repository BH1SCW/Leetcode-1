from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        window = deque()
        result = []
        for i in range(k):
            # the order matters so much, always append, delete only after there are something larger after
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)
        if window:
            result.append(nums[window[0]])
        for i in range(k, n):
            # update the window
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)
            # update and return the maximum
            while window and window[0] <= i - k:
                window.popleft()
            result.append(nums[window[0]])
        return result

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    nums = []
    k = 0
    sol = Solution()
    print(sol.maxSlidingWindow(nums, 0))





