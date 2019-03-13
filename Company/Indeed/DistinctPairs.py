def numberOfPairs(a, k):
    # Write your code her
    a.sort()
    i = 0
    j = len(a)- 1
    ans = 0
    while (True):
        if j > 0 and a[j - 1] == a[j]:
            j -= 1
            continue
        if i < len(a) - 1 and a[i + 1] == a[i]:
            i += 1
            continue
        if i == j:
            break;
        if j > 0 and a[j - 1] == a[j] and 2 * a[j] == k:
            ans += 1
        if i < len(a) - 1 and a[i + 1] == a[i] and 2 * a[i] == k:
            ans += 1
        if i > j:
            if a[i] == a[j] and a[i] + a[j] == k:
                ans += 1
            break
        if a[i] + a[j] == k:
            ans += 1
            i += 1
            j -= 1
            continue
        if a[i] + a[j] < k:
            i += 1
        else:
            j -= 1
    return ans

