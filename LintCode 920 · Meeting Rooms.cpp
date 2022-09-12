class Solution {
public:
    bool canAttendMeetings(vector<Interval> &intervals) {
        if (intervals.empty()) return true;
        sort(intervals.begin(), intervals.end(), [](const Interval &i1, const Interval &i2){return i1.start < i2.start;});
        for(int i = 0; i < intervals.size() - 1; i++){
            if(intervals[i + 1].start < intervals[i].end){
                return false;
            }
        }
        return true;
    }
};