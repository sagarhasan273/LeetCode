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