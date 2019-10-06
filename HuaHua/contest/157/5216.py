from __future__ import annotations
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {'a':1, 'e':2, 'i':4, 'o':2, 'u':1}
        endings = {}
        for k in rules.keys():
            endings[k] = 1
        for i in range(2, n + 1):
            new = {}
            new['a'] = endings['e'] + endings['u'] + endings['i']
            new['e'] = endings['a'] + endings['i']
            new['i'] = endings['e'] + endings['o']
            new['o'] = endings['i']
            new['u'] = endings['o'] + endings['i']
            endings = new
        return sum(endings.values()) % (10**9 + 7)

if __name__ == '__main__':
    sol = Solution()
    n = 1
    n = 2
    n = 144
    print(sol.countVowelPermutation(n))
