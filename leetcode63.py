class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                if (r, c) in memo:
                    return memo[(r, c)]
                
                if obstacleGrid[r][c] == 1:
                    return 0
                
                if r+1 == rows and c+1 == cols:
                    return 1
                
                memo[(r, c)] = dfs(r+1, c) + dfs(r, c+1)
                return memo[(r, c)]
            
            return 0
    
        return dfs(0, 0)