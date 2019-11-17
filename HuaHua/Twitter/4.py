def isPossible(calCounts, requiredCals):
    dp = [1] + [0] * requiredCals
    calCounts.sort()
    for c in calCounts:
        for i in range(c, len(dp))[::-1]:
            dp[i] = dp[i] or dp[i - c]
    return dp[-1]

