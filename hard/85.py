class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # if_debug = True
        w = len(matrix)
        if w == 0:
            return 0
        l = len(matrix[0])
        hash = {}
        max = 0
        for sw in range(1, w + 1):
            for sl in range(1, l + 1):
                for i in range(w):
                    for j in range(l):
                        # the rec must be legal
                        if i + sw - 1 < w and j + sl - 1 < l:
                            if sw == 1:
                                if sl == 1:
                                    rec = int(matrix[i][j])
                                    # hash[((i, j), (i, j))] = rec
                                    # if rec > max:
                                    #     max = rec
                                else:
                                    small_rec1 = ((i, j), (i, j + sl - 2))
                                    small_rec2 = ((i, j + sl - 1), (i, j + sl - 1))
                                    rec = hash[small_rec1] and hash[small_rec2]
                                    # hash[(i, j), (i + sw  - 1, j + sl - 1)] = hash[small_rec1] and hash[small_rec2]
                                    # if rec:
                                    #     if if_debug:
                                    #         print(('shape: {} x {}').format(sw, sl))
                                    #         print(small_rec1)
                                    #         print(small_rec2)
                                    #         print((i, j), (i + sw - 1, j + sl - 1))
                                    #     if sw * sl > max:
                                    #         max = sw * sl
                            else:
                                small_rec1 = ((i, j), (i + sw - 2, j + sl - 1))
                                small_rec2 = ((i + sw - 1, j), (i + sw - 1, j + sl - 1))
                                rec = hash[small_rec1] and hash[small_rec2]
                                # hash[(i, j), (i + sw - 1, j + sl - 1)] = rec
                            hash[(i, j), (i + sw - 1, j + sl - 1)] = rec
                            if rec:
                                # if if_debug:
                                #     print(('shape: {} x {}').format(sw, sl))
                                #     print(small_rec1)
                                #     print(small_rec2)
                                #     print((i, j), (i + sw - 1, j + sl - 1))
                                if sw * sl > max:
                                    max = sw * sl
        # if if_debug:
        #     print(max)
        return max

if __name__ == '__main__':
    m=[["1","0","1","0","0"],
       ["1","0","1","1","1"],
       ["1","1","1","1","1"],
       ["1","0","0","1","0"]]
    m = [["1"]]
    sol = Solution()
    sol = sol.maximalRectangle(m)

