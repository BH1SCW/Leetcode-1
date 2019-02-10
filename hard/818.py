from collections import deque
class Solution:
    def racecar(self, target: 'int') -> 'int':
        q = deque()
        q.append((1, target, 0, ""))
        # q.append((1, target, 0))
        def helper(initial, aim, steps, actions):
        # def helper(initial, aim, steps):
            q.append((initial, aim, steps, actions))
            # q.append((initial, aim, steps))
            if aim == 0:
                q.appendleft((initial, aim, steps, actions))
                # q.appendleft((initial, aim, steps))
                print(actions)
                return True
        while q:
            # speed, aim, action = q.pop()
            # if action == 'A':
            speed, aim, steps, actions = q.popleft()
            # speed, aim, steps = q.popleft()
            if helper(speed * 2, aim - speed, steps + 1, actions + "A"):
            # if helper(speed * 2, aim - speed, steps + 1):
                break
            # if not(not steps and speed == 1):
            # if helper(-1 if speed > 0 else 1, aim, steps + 1, actions + "R"):
            if (speed != 1 or not steps) and helper(-1 if speed > 0 else 1, aim, steps + 1, actions + "R"):
            # if (speed != 1 or not steps) and helper(-1 if speed > 0 else 1, aim, steps + 1):
            # if helper(-1 if speed > 0 else 1, aim, steps + 1):
                break
        return q[0][2]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.racecar(3))
    print(sol.racecar(432))


