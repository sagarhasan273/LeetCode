class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [None] * length
        dp[0] = nums[0]
        
        size = 0
        
        for i in range(length):
            if nums[i] > dp[size]:
                dp[size+1] = nums[i]
                size += 1
            else:
                l = 0
                r = size
                index = None
                
                while l <= r:
                    mid = (l+r) // 2
                    if dp[mid] >= nums[i]:
                        index = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                dp[index] = nums[i]
        
        return size + 1