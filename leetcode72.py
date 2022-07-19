class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        def dfs(i,j):
            if i==len(word1):
                return len(word2)-j
            
            if j==len(word2):
                return len(word1)-i
            
            if(dp[i][j]!=-1):
                return dp[i][j]
            
            if(word1[i]==word2[j]):
                dp[i][j] = dfs(i+1,j+1)
                return dp[i][j]
            
            dp[i][j] = min(dfs(i+1,j), dfs(i,j+1), dfs(i+1,j+1)) + 1
            return dp[i][j]
        
        return dfs(0,0)