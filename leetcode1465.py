class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        horizontalCuts.sort()
        verticalCuts.sort()
        
        p, q = 0, 0
        for i in range(1, len(horizontalCuts)):
            p = max(p, horizontalCuts[i]-horizontalCuts[i-1])

        for j in range(1, len(verticalCuts)): 
            q = max(q, verticalCuts[j]-verticalCuts[j-1])
        
        return (p*q) % (10**9 + 7)