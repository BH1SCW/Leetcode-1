class Solution(object):
    # 这个做法还是比较精妙的，非常简洁
    # https://leetcode.com/problems/spiral-matrix/
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j, di, dj = 0, 0, 0, 1
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i + di) % m][(j + dj) % n] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return ans


if __name__ == '__main__':
    sol = Solution()
    matrix = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    print(sol.spiralOrder(matrix))
