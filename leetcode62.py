class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]
        
        for i in range(1, m):
            dp = [1]*n
            for j in range(1, n):
                dp[j] = row[j] + dp[j-1] if j-1 >= 0 else dp[j]
            row = dp
        
        return row[-1]