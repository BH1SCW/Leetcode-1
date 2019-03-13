from collections import deque
def alert(inputs, windowSize, allowedIncrease):
    maximums = deque([])
    for i in range(windowSize):
        maximums.append(i)
        while (len(maximums) > 1 and inputs[maximums[-1]] >= inputs[maximums[-2]]):
            maximums[-1], maximums[-2] = maximums[-2], maximums[-1]
            maximums.pop()
    prev_sum = sum(inputs[:windowSize])
    cur_sum = prev_sum
    max_local = max(inputs[:windowSize])
    times = {}
    if max_local / (cur_sum / windowSize) > allowedIncrease:
        return True
    for st in range(windowSize, len(inputs)):
        prev_sum = cur_sum
        cur_sum = cur_sum - inputs[st - windowSize] + inputs[st]
        while (maximums[0] <= st - windowSize):
            maximums.popleft()
        maximums.append(st)
        while (len(maximums) > 1 and inputs[maximums[-1]] >= inputs[maximums[-2]]):
            maximums[-1], maximums[-2] = maximums[-2], maximums[-1]
            maximums.pop()
        max_local = maximums[0]
        if inputs[max_local] / (cur_sum / windowSize) > allowedIncrease:
            if not max_local in times:
                times[max_local] = 1
            else:
                times[max_local] += 1
            if times[max_local] == windowSize:
                return True
        if cur_sum / prev_sum > allowedIncrease:
            return True
    return False

if __name__ == '__main__':
    inputs = [1, 2, 100, 2, 2]
    windowSize = 3
    allow = 1.5
    # inputs = [1,2,100,2,2]
    # windowSize = 2
    # allow = 2.5
    # inputs = [1, 2, 100, 2, 2]
    # windowSize = 3
    # allow = 1.5
    print(alert(inputs, windowSize, allow))


