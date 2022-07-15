class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = [0]
        l = len(coins)
        coins.sort(reverse=True)
        memo = {}
        
        def dfs(r, i):
            if (r, i) in memo:
                return memo[(r, i)]
            
            if r > amount or i >= l:
                return 0

            if r == amount:
                return 1
            
            c1 = dfs(r+coins[i], i)
            c2 = dfs(r, i+1)
            memo[(r, i)] = c1 + c2
            
            return memo[(r, i)]

        return dfs(0, 0)
            