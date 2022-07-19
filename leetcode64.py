class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        for i in range(1, cols):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, rows):
            for j in range(cols):
                down = grid[i][j-1] if j-1 >= 0 else 999
                up = grid[i-1][j] if i-1 >= 0 else 999
                grid[i][j] = grid[i][j] + min(up, down)
        
        return grid[-1][-1]