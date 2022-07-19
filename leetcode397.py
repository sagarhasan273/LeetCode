class Solution:
    def integerReplacement(self, n: int) -> int:

        def dfs(n):
            if n == 1:
                return 0
            
            if n%2:
                return 1 + min(1+self.integerReplacement((n+1)//2), 1+self.integerReplacement((n-1)//2))
            
            return 1 + self.integerReplacement(n//2)
        
        return dfs(n)