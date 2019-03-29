from collections import deque
# author: Xianglong Hu
# speed: 79%
class Solution:
    def openLock(self, deadends: 'List[str]', target: str) -> int:
        q1 = deque(['0000'])
        q2 = deque([target])
        searched = [0] * 10000
        moves = {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        def neightbors(s):
            for i, c in enumerate(s):
                for n in (s[0:i] + moves[c][0] + s[i + 1:], s[0:i] + moves[c][1] + s[i + 1:]):
                    if not n in deadends:
                        yield n

        step = 0
        while q1 and q2:
            if (len(q1) > len(q2)):
                q1, q2 = q2, q1
            q = deque([])
            for e in q1:
                for n in neightbors(e):
                    if n in q2:
                        return step + 1
                    else:
                        try:
                            if not searched[int(n)]:
                                q.append(n)
                                searched[int(n)] = 1
                        except:
                            print(n)
            step += 1
            q1 = q
        return -1


if __name__ == '__main__':
    sol = Solution()
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(sol.openLock(deadends, target))
