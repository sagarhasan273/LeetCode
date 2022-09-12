class Solution {
public:

    int minMeetingRooms(vector<Interval> &intervals) {
        map<int, int> m;
        int ans=0, pre=0;

        for (auto& [f, s]: intervals){
            m[f]++;
            m[s]--;
        }

        for (auto& x: m){
            pre += x.second;
            ans = max(ans, pre);
        }
        return ans;

    }
};








#include<map>

class Solution {
public:

    int minMeetingRooms(vector<Interval> &intervals) {
        vector<int> starts, ends;
        for(auto& [f, s]: intervals){
            starts.push_back(f);
            ends.push_back(s);
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        int i = 0, j = 0, count = 0, mx = 0;

        while (i<starts.size() and j<=i){
            if (starts[i] < ends[j]){
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