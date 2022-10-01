class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end()), ans=0, count=0;
        
        for (auto &x: nums){
            if (x == mx) count++;
            else count = 0;
            ans = max(ans, count);
        }
        
        return ans;
    }
};