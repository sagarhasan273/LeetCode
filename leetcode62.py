class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if j-1 >= 0 else dp[i-1][j]
        
        return dp[-1][-1]