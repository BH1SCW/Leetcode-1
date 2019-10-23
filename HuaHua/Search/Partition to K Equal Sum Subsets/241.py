class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def helper(input):
            ans, is_number = [], True
            for i, c in enumerate(input):
                if c == '*' or c == '+' or c == '-':
                    is_number = False
                    left, right = helper(input[:i]), helper(input[i + 1:])
                    ans += [eval(l + c + r) for l in left for r in right]
            if is_number:
                return [int(input)]
            return ans
        return [int(s) for s in helper(input)]


