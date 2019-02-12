class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        lb = 0
        for i in range(len(s)):
            if len(s) - i < res or i < lb:
                continue
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    lb = j
                    break
            res = max(j - i, res)
        return res

if __name__ == '__main__':
    nums ="abcabcbb"
    nums = "bbbbb"
    nums = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(nums))

