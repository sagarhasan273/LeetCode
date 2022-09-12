class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        priority_queue<int, vector<int>, greater<int>> pq;
        
        sort(intervals.begin(), intervals.end());
        
        int N = intervals.size();
        pq.push(intervals[0][1]);
        
        for (int i=1; i<N; i++){
            if (intervals[i][0] <= pq.top()){
                pq.push(intervals[i][1]);
            }else{
                pq.pop();
                pq.push(intervals[i][1]);
            }
        }
        return pq.size();
    }
};


