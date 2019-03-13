def maxPoints(elements):
    i = 0
    j = 1
    points = [0] * 10001
    for e in elements:
        points[e] += e
    last, now = 0, 0
    for i in points:
        last, now = now, max(last + i, now)
    return now

