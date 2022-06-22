class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def helper(i, arr, total):
            if total > target or i >= n:
                return
            if total == target:
                res.append(arr)
                return
            
            helper(i, arr+[candidates[i]], total+candidates[i])
            helper(i+1, arr, total)
            
        
        helper(0, [], 0)
        return res