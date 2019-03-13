def palindrome(s):
    ans = set()
    # if len(s) == 0:
    #     return 0
    def find(i, j, ans):
        k = i - 1
        l = j + 1
        while k >= 0 and l < len(s):
            if s[k] == s[l]:
                ans.add(s[k:l + 1])
                k -= 1
                l += 1
            else:
                break
    for i in range(len(s)):
        ans.add(s[i])
        find(i, i, ans)
        if i <= len(s) - 2 and s[i] == s[i + 1]:
            ans.add(s[i:i + 2])
            find(i, i + 1, ans)
    print(ans)
    return len(ans)

if __name__ == '__main__':
    s = "aabaa"
    s = "abaab"
    # s = "mokkori"
    # s = ""
    s = "aba"
    print(palindrome(s))


