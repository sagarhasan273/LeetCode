class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = list(range(1, n+1))

        def dfs(i, res):
            if len(res) == k:
                ans.append(res)
                return
            
            if i < 0 or i >= n:
                return

            dfs(i+1, res+[nums[i]])
            dfs(i+1, res)
        
        dfs(0, [])
        return ans