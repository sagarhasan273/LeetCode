class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)
        dp=[[-1]*(w2+1) for _ in range(w1+1)]

        def dfs(i,j):
            if i == w1:
                return w2-j
            
            if j == w2:
                return w1-i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = dfs(i+1,j+1)
                return dp[i][j]
            
            dp[i][j] = min(dfs(i+1,j), dfs(i,j+1), dfs(i+1,j+1)) + 1
            return dp[i][j]
        
        return dfs(0,0)