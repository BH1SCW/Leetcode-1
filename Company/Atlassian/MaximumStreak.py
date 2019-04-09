def maxStreak(m, data):
    all_present = 'Y' * m
    count, ans = 0, 0
    for d in data:
        if d == all_present:
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    return ans


if __name__ == '__main__':
    m = 3
    data = ['YYY', 'YYY', 'YNN', 'YYN', 'YYN']
    m = 2
    data = ['YN', 'NN']
    m = 3
    data = ['NYY']
    print(maxStreak(m, data))
