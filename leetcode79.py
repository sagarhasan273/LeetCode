class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        res = [0]
        visited = set()
        
        def dfs(row, col, i, s):
            if s == word:
                res[0] = 1
                return
            
            if i >= len(word) or min(row, col) < 0 or row >= rows or col >= cols or (row, col) in visited or board[row][col] != word[i]:
                return

            visited.add((row, col))
            for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                    dfs(r, c, i+1, s+word[i])
            visited.remove((row, col))
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    dfs(i, j, 0, "")
        
        return res[0]