def findBestPath(n, m, max_t, beauty, u, v, t):
    neighbors = {}
    weights = {}
    ans = 0
    for i in range(m):
        neighbors[u[i]] = neighbors[u[i]] + [v[i]] if u[i] in neighbors else [v[i]]
        neighbors[v[i]] = neighbors[v[i]] + [u[i]] if v[i] in neighbors else [u[i]]
        weights[(u[i], v[i])], weights[(v[i], u[i])] = t[i], t[i]
    def dfs(start, time_left, beauties):
        nonlocal ans
        if start == 0 and time_left >= 0:
            ans = max(ans, beauties)
        for nb in neighbors.get(start, None):
            if weights[(start, nb)] <= time_left:
                b, beauty[nb] = beauty[nb], 0
                dfs(nb, time_left - weights[(start, nb)], beauties + b)
                beauty[nb] = b
    b, beauty[0] = beauty[0], 0
    dfs(0, max_t, b)
    return ans

if __name__ == '__main__':
    n = 4
    m = 3
    max_t = 30
    beauty = [5, 10, 15, 10]
    u = [0, 1, 0]
    v = [1, 2, 3]
    t = [6, 7, 10]

    n = 4
    m = 3
    max_t = 49
    beauty = [0, 32, 10, 43]
    u = [0, 2, 0]
    v = [1, 0, 3]
    t = [10, 13, 17]

    print(findBestPath(n, m, max_t, beauty, u, v, t))

