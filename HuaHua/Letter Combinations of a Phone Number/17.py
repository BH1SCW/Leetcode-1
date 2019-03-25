class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = ['']
        for d in digits:
            new = [a + m for m in mapping[d] for a in ans]
            ans = new
            # for a in ans:
            #     for m in mapping[d]:
            #         new.append(a + m)
        return ans

if __name__ == '__main__':
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
