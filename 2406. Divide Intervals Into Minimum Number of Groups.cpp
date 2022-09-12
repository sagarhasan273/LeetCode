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



another solution:


class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        map<int, int> m;
        int ans=0, count=0;
        
        for (auto& x: intervals){
            m[x[0]]++;
            m[x[1]+1]--;
        }
        
        for(auto& x: m){
            count += x.second;
            ans = max(ans, count);
        }
        
        return ans;
    }
};



class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        vector<int> starts, ends;
        for(auto& x: intervals){
            starts.push_back(x[0]);
            ends.push_back(x[1]);
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        int i = 0, j = 0, count = 0, mx = 0;

        while (i<starts.size() and j<=i){

            if (starts[i] <= ends[j]){
                count++;
                i++;
            }
            else{
                count--;
                j++;
            }
            mx = max(mx, count);
        }
        return mx;
    }
};


