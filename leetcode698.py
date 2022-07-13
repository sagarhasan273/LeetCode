class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k:
            return False
        
        nums.sort(reverse=True)
        
        target = sum(nums)/k
        used = [False] * len(nums)
        
        def backTracking(i, k, subSum):
            if k == 0:
                return True
            if subSum == target:
                return backTracking(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or subSum + nums[j] > target:
                    continue
                
                used[j] = True
                if backTracking(j+1, k, subSum + nums[j]):
                    return True
                used[j] = False
                
            return False
        
        return backTracking(0, k, 0)
        
        
        
        
        