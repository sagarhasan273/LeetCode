class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hashMap = {}
        intervals.sort()

        minHeap = []

        i_l = len(intervals)
        i = 0
        for q in sorted(queries):
            while i < i_l and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minHeap, [(end-start+1), end])
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            hashMap[q] = minHeap[0][0] if minHeap else -1

        return [hashMap[q] for q in queries]