class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        
        def dfs(n):
            if n == 1:
                return 0
            
            if n in memo:
                return memo[n]
            
            if n%2:
                memo[n] = 1 + min(1+self.integerReplacement((n+1)//2), 1+self.integerReplacement((n-1)//2))
                return memo[n]
            
            memo[n] = 1 + self.integerReplacement(n//2)
            return memo[n]
        
        return dfs(n)