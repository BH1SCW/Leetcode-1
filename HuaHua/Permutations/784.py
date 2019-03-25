class Solution:
    def letterCasePermutation(self, S: str) -> 'List[str]':
        # if not S:
        #     return []
        ans = ['']
        S = S.lower()
        for s in S:
            new = [a + s for a in ans]
            if s >= 'a' and s  <= 'z':
                new += [a + s.upper() for a in ans]
            ans = new
        return ans

if __name__ == '__main__':
    sol = Solution()
    S = "a1b2"
    S = "12345"
    S = "3z4"
    print(sol.letterCasePermutation(S))
