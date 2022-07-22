class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        que = deque()
        time, fresh = 0, 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    que.append([i, j])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while que and fresh > 0:
            
            for _ in range(len(que)):
                r, c = que.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    
                    if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    que.append([row, col])
                    fresh -= 1
            time += 1
        
        return -1 if fresh else time
                       
        