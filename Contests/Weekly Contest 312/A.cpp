class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<string> ans;
        vector<pair<string, int>> tall;
        
        int n = names.size();
        
        for(int i = 0; i < n; i++) tall.push_back({names[i], heights[i]});
        
        sort(tall.begin(), tall.end(), [](auto a, auto b){
            return a.second > b.second;
        });
        
        for (auto &x: tall) ans.push_back(x.first);
        
        return ans;
    }
};