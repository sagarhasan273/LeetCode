class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for _ in range(n)]
        count = [0]
        col = set()
        posDiag = set()
        negDiag = set()
        
        def backTrack(r):
            if r == n:
                count[0] += 1
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                backTrack(r+1)
                
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        backTrack(0)
        
        return count[0]
            