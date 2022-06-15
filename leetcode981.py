class TimeMap:
    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap.keys():
            self.timeMap[key].append([timestamp, value])
        else:
            self.timeMap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key, [])

        left, right = 0, len(values)-1
        res = ""
        while left <= right:
            mid =left + ((right-left)//2)
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)