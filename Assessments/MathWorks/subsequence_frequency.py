def getSubsequenceCount(s1, s2):
    s2, s1 = s1, s2 
    row = len(s1) 
    col = len(s2) 
  
    dp = [[0] * (col + 1) for i in range(row + 1)] 
  
    for i in range(col+1): 
        dp[0][i] = 0
  
    for i in range(row + 1): 
        dp[i][0] = 1
  
    for i in range(1, row + 1): 
        for j in range(1, col + 1): 
            if s1[i - 1] == s2[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  
            else: 
                dp[i][j] = dp[i - 1][j] 
    
    return dp[-1][-1] 

if __name__ == "__main__":
    print(getSubsequenceCount('HRW','HERHRWS'))