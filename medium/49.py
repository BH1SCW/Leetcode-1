class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for s in strs:
            try:
                map[tuple(sorted(s))] += [s]
            except:
                map[tuple(sorted(s))] = [s]
        return list(map.values())

if __name__ == '__main__':
    nums ="abcabcbb"
    nums = "bbbbb"
    nums = "pwwkew"
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))

