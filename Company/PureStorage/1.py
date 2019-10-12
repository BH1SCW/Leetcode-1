from collections import deque
def compute_number_score(number):
    digits = deque([])
    score = 6 if number % 5 == 0 else 0  # rule 4
    while number > 0:
        digits.appendleft(number % 10)
        number //= 10
    prev, first_three, end_three, first_seq, end_seq = -1, 0, 0, 0, 0
    for i in range(len(digits)):
        d = digits[i]
        if d == 5:
            score += 2  # rule 1
        if d % 2:
            score += 1  # rule 5
        if d == 3:  # rule 2
            if prev != 3:
                first_three, end_three = i, i
            else:
                end_three = i
        elif prev == 3:
            score += max(0, (end_three - first_three) * 4)
            first_three, end_three = i, i
        else:
            first_three, end_three = i, i
        if i:
            if d == prev + 1:
                end_seq = i
            else:
                score += max(0, (end_seq - first_seq + 1) * (end_seq - first_seq  + 1))
                first_seq, end_seq = i, i
        prev = d
    score += max(0, (end_three - first_three) * 4)
    score += max(0, (end_seq - first_seq + 1) * (end_seq - first_seq  + 1))
    return score

if __name__ == '__main__':
    number = 456
    print(compute_number_score(number))
