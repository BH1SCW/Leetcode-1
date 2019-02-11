from collections import deque
class Solution:
    def racecar(self, target: 'int') -> 'int':
        q = deque()
        q.append((1, target, 0))
        found = set()
        def helper(initial, aim, steps):
            if (initial, aim) in found:
                return
            else:
                found.add((initial, aim))
            q.append((initial, aim, steps))
            if aim == 0:
                q.appendleft((initial, aim, steps))
                return True
            return
        while q:
            speed, aim, steps = q.popleft()
            if helper(speed * 2, aim - speed, steps + 1):
                break
            # if (aim <= 0 or (aim >= 0 and speed < 0)) and helper(-1 if speed > 0 else 1, aim, steps + 1):
            if ((aim < 0 and speed > 0) or (aim >= 0 and speed < 0)) and helper(-1 if speed > 0 else 1, aim, steps + 1):
                break
        return q[0][2]


if __name__ == '__main__':
    sol = Solution()
    print(sol.racecar(4))
    # print(sol.racecar(432))


