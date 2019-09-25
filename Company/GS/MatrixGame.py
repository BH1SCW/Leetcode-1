def play(arr):
    transpose = list(map(list, zip(*arr)))
    maxs = [max(col) for col in transpose]
    maxs.sort(reverse=True)
    # if len(maxs) % 2 != 0:
    #     maxs = maxs[:-1]
    s = sum(maxs)
    first_player_score, i = 0, 0
    while i <= len(maxs) - 1:
        first_player_score += maxs[i]
        i = i + 2
    second_player_score = s - first_player_score
    return first_player_score - second_player_score


if __name__ == '__main__':
    x=[[5,7,6,2,8,4,4,8],[2,5,4,5,9,8,4,2,],[5,4,3,9,8,3,3,4,],[4,9,3,4,6,7,4,9,],[2,4,6,2,9,2,4,2,]]
    print(play(x))

