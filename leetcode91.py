class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)  
        dp = {l: 1}
        
        for i in range(l-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i+1 < l and (s[i] == "1" or (s[i] == '2' and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]