class Solution:
    def piecesCounter(self, grid) -> int:
        n = len(grid)
        self.white, self.blue = 0, 0

        def countWhiteBlue(grid, startI, startJ, size):
            check = grid[startI][startJ]
            for r in range(startI, startI+size):
                for c in range(startJ, startJ+size):
                    if check != grid[r][c]:
                        return False
            return True

        def dfs(grid, startI, startJ, size):

            if not countWhiteBlue(grid, startI, startJ, size):
                dfs(grid, startI, startJ, size//2)
                dfs(grid, startI+size//2, startJ, size//2)
                dfs(grid, startI, startJ+size//2, size//2)
                dfs(grid, startI+size//2, startJ+size//2, size//2)
            else:
                if grid[startI][startJ]:
                    self.blue += 1
                else:
                    self.white += 1
        
        dfs(grid, 0, 0, n)

        return [self.white, self.blue]



    def main(self):
        for _ in range(int(input())):
            n = int(input())
            grid = []
            for i in range(n):
                grid.append(list(map(int, input().split())))
            print(*self.piecesCounter(grid))

Solution().main()
