# T[i][j] refers to the minial distance to 0
# so T[i][j] = min(minDis(i - 1, j), minDis(i +  1, j), minDis(i, j - 1), minDis(i, j + 1)) + 1
# minDis return the minimal distance
# if matrix[i][j] == 0: return 0, else return the same procedure
# to reduce the work, we have to mark i, j as searched to avoid repeated work

