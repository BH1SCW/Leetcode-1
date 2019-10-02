class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for e in arr:
            if e in dict:
                dict[e] += 1
            else:
                dict[e] = 1
        n = len(dict)
        m = len(set(dict.values()))
        return m == n