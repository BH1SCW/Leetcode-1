def exam(v):
    score = [1 if n == 1 else -1 for n in v]
    total = sum(score)
    s = 0
    target = total // 2 + 1
    for i, n in enumerate(score):
        if s >= target:
            return i
        s += n
    return i

