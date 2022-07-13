class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        
        for i in range(len(s)):
            last[s[i]] = i

        start, end, res = 0, 0, []
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if i == end:
                res.append((end-start)+1)
                start = i+1
        
        return res
        