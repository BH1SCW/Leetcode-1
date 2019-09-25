def gridGame(grid, k, rules):
    alive = set([r for r in range(len(rules)) if rules[r] == 'alive'])
    rows, cols = len(grid), len(grid[0])
    def neighbors(r, c):
        for row, col in (r - 1, c), (r + 1, c), (r, c - 1), (r, c+ 1), (r - 1, c - 1), (r + 1, c - 1), (r - 1, c + 1), (r + 1, c + 1):
            if 0 <= row < rows and 0 <= col < cols:
                yield (row, col)

    def proceed(arr):
        stats = [[0] * cols for r in range(rows)]
        for i in range(rows):
            for j in range(cols):
                for r, c in neighbors(i, j):
                    if arr[r][c]:
                        stats[i][j] += 1
        for i in range(rows):
            for j in range(cols):
                if stats[i][j] in alive:
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

    for i in range(k):
        proceed(grid)
    return grid

