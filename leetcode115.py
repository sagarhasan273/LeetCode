class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        r, c = len(t), len(s)
        dp = [[0]*c for _ in range(r)]
        
        for i in range(c):
            dp[0][i] = 1 + dp[0][i-1] if t[0] == s[i] else dp[0][i-1]
        
        for i in range(1, r):
            for j in range(1, c):
                
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] if t[i] == s[j] else dp[i][j-1]
  
        return dp[-1][-1]