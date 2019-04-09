# def arraysCount(n, m, totalCost):
#     ans = []
#     memo = {}
#     for ni, mi, ti in zip(n, m, totalCost):
#         ans.append(reconstrcut(ni, mi, ti, memo))
#     return ans
#
# def reconstrcut(n, m, totalCost, memo):
#     if (n, m, totalCost) in memo:
#         return memo[(n, m, totalCost)]
#     ans = 0
#     def dfs(index, cost, prev):
#         nonlocal ans
#         if index == n:
#             if cost == 0:
#                 ans += 1
#             return
#         if cost < 0:
#             return
#         for num in range(1, m + 1):
#             if num > prev:
#                 dfs(index + 1, cost - 1, num)
#             else:
#                 dfs(index + 1, cost, prev)
#     dfs(0, totalCost + 1, 0)
#     memo[(n, m, totalCost)] = ans
#     return ans

large_number = int(1e9) + 7

def arraysCount(n, m, totalCost):
    ans = []
    memo = {}
    for ni, mi, ti in zip(n, m, totalCost):
        ans.append(reconstrcut(ni, mi, ti, memo))
    return ans

def reconstrcut(n, m, totalCost, memo):
    if (n, m, totalCost) in memo:
        return memo[(n, m, totalCost)]
    ans = 0
    def dfs(index, cost, prev):
        nonlocal ans
        old = ans
        if (n - index, m, cost, prev) in memo:
            ans += memo[(n - index, m, cost, prev)]
            ans %= large_number
            return
        if index == n:
            if cost == 0:
                ans += 1
            return
        if cost < 0:
            return
        for num in range(1, prev + 1):
            dfs(index + 1, cost, prev)
        for num in range(prev + 1, m + 1):
            dfs(index + 1, cost - 1, num)
        # for num in range(1, m + 1):
        #     if num > prev:
        #         dfs(index + 1, cost - 1, num)
        #     else:
        memo[(n - index, m, cost, prev)] = (ans - old) % large_number
    dfs(0, totalCost + 1, 0)
    memo[(n, m, totalCost)] = ans % large_number
    return (ans % (int(1e9) + 7))

def getPeak(cost, m):
    combinations = [[i] for i in range(1, m + 1)]
    for i in range(cost - 1):
        new = []
        for c in combinations:
            for n in range(c[-1] + 1, m + 1):
                new += [c + [n]]
        combinations = new
    return combinations

def getSpace(n, cost):
    ans = []
    def dfs(total, path, number, ans):
        if number == 1:
            ans += [path + [total]]
            return
        for i in range(total + 1):
            dfs(total - i, path + [i], number - 1, ans)
    dfs(n, [], cost + 1, ans)
    return ans

def construct(n, m, cost):
    peaks = getPeak(cost, m)
    spaces = getSpace(n, cost)
    ans = 0
    for peak in peaks:
        for space in spaces:
            for i in range(0, cost):
                if peak[i] < space[i]:
                    break
            peak[i] >


if __name__ == '__main__':
    print(getPeak(3, 4))
    print(getSpace(4, 2))
    n = 4
    m = 4
    totalCost = 2
    print(reconstrcut(n, m, 2, {}))
    n = [2, 3, 4]
    m = [3, 3, 3]
    totalCost = [1, 2, 2]
    print(arraysCount(n, m, totalCost))

