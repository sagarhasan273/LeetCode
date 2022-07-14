class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cor = int(correct[:2])*60 + int(correct[3:])
        cur = int(current[:2])*60 + int(current[3:])
        convert = cor - cur
        
        minutes = [60, 15, 5, 1]
        
        count,i = 0, 0
        
        while convert and i != 4:
            if minutes[i] <= convert:
                count += convert // minutes[i]
                convert = convert % minutes[i]
            i += 1
        
        return count
        