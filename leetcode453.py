class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ele = min(nums)
        moves = 0
        
        for n in nums:
            moves += abs(min_ele - n)
        return moves
            