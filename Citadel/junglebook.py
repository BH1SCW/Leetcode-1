def minimumGroups(predators):
    # Write your code here
    length = {}
    ans = 0
    def dfs(i):
        if not i in length:
            if i == -1:
                length[i] = 1
            else:
                length[i] = dfs(predators[i]) + 1
        return length[i]
    for i in predators:
        if not i in length:
            ans = max(ans, dfs(i))
        else:
            continue
    return ans


if __name__ == '__main__':
    a = [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]
    print(minimumGroups(a))
