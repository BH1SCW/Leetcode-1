class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def remove(counter, ns, i):
            counter = counter[:i] + counter[i + k:]
            ns = ns[:i] + ns[i + k:]
            ni = i
            if i >= 1 and ns[i - 1] == ns[i]:
                counter[i][0] += counter[i - 1][0]
                if counter[i][0] >= k:
                    ni = i - counter[i - 1][0]
                counter[i - 1][0] += counter[i][0]
            return (counter, ns, ni)

        ptr = [1]
        counter = []
        n = len(s)
        for i in range(1, n):
            counter.append(ptr)
            if s[i] != s[i - 1]:
                ptr = [1]
            else:
                ptr[0] += 1
        i = 0
        while i <= n:
            if i >= len(counter):
                break
            if counter[i][0] >= k:
                counter, s, i = remove(counter, s, i)
            else:
                i += 1
        return s

if __name__ == '__main__':
    sol = Solution()
    s = "pbbcggttciiippooaais"
    k = 2
    print(sol.removeDuplicates(s, k))



