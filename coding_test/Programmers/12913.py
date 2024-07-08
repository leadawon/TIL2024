def solution(land):
    answer = 0

    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    
    for i in range(len(land)):
        if i ==0:
            for j in range(4):
                dp[0][j] = land[0][j]
        else:
            dp[i][0] = max(dp[i-1][1],dp[i-1][2],dp[i-1][3]) + land[i][0]
            dp[i][1] = max(dp[i-1][0],dp[i-1][2],dp[i-1][3]) + land[i][1]
            dp[i][2] = max(dp[i-1][1],dp[i-1][0],dp[i-1][3]) + land[i][2]
            dp[i][3] = max(dp[i-1][1],dp[i-1][2],dp[i-1][0]) + land[i][3]
    answer = max(dp[-1][0],dp[-1][1],dp[-1][2],dp[-1][3])
                

    return answer