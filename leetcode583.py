class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1)+1, len(word2)+1
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            dp[r][0] = 1 + dp[r-1][0] if r else 0
        
        for c in range(cols):
            dp[0][c] = 1 + dp[0][c-1] if c else 0
        
        for row in range(1, rows):
            for col in range(1, cols):
                if word1[row-1] == word2[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = 1 + min(dp[row-1][col], dp[row][col-1])

        return dp[-1][-1]