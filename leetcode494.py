class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        total = sum(nums)
        memo = [[-1 for _ in range(l)] for _ in range(2*(total+1))]
        
        
        def dfs(sumNum, i):
            if sumNum == target and sumNum <= total and i == l:
                return 1
            
            if i >= l:
                return 0
            
            if memo[sumNum+total][i] != -1:
                return memo[sumNum+total][i]
            
            memo[sumNum+total][i] = dfs(sumNum+nums[i], i+1) + dfs(sumNum-nums[i], i+1)
            return memo[sumNum+total][i]
        
        return dfs(0, 0)
        