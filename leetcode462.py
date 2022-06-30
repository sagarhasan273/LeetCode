class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        m = len(nums)//2
        total = 0
        for i in nums:
            total += abs(i - nums[m])
        return total
       