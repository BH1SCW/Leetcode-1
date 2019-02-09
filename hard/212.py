class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        initials = set()
        word = set(words)
        passed = set()
        res = set()
        for w in words:
            for end in range(1, len(w) + 1):
                initials.add(w[0:end])
        h = len(board)
        l = len(board[0])
        def helper(i, j, w):
            # print(i, j, w)
            if (i, j) in passed:
                return
            if w + board[i][j] in word:
                res.add(w + board[i][j])
            if w and not w + board[i][j] in initials:
                return
            passed.add((i, j))
            if i > 0:
                helper(i - 1, j, w + board[i][j])
            if i < h - 1:
                helper(i + 1, j, w + board[i][j])
            if j > 0:
                helper(i, j - 1, w + board[i][j])
            if j < l - 1:
                helper(i, j + 1, w + board[i][j])
            passed.remove((i, j))
        for x in range(h):
            for y in range(l):
                if board[x][y] in initials:
                    helper(x, y, "")
                else:
                    continue
        return list(res)


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
    # words = ["a"]
    # board = [["a", "a"]]
    words = ["aaa"]
    board = [["a", "a"]]
    words = ["aaab", "aaba"]
    words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
    board = [["a", "b"], ["a", "a"]]
    sol = Solution()
    print(sol.findWords(board, words))
