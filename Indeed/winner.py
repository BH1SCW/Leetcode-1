def winner(andrea, maria, s):
    start = 0
    if s == "ODD":
        start = 1
    a = 0
    m = 0
    for i in range(start, len(andrea), 2):
        a += andrea[i] - maria[i]
        m += maria[i] - andrea[i]
    if a > m:
        return "Andrea"
    if a == m:
        return "Tie"
    return "Maria"

if __name__ == '__main__':
    a = [3, 1, 2, 3]
    m = [3, 2, 1, 3]
    winner(a, m, "ODD")
