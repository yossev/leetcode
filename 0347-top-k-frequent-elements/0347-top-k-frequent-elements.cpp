class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;    

        for (int n: nums) {
            freq[n]++;
        }

        vector<int> result;

        while(k--) {
            int bestKey = 0;
            int bestFreq = -1;


            for(auto &p: freq){
                if (p.second > bestFreq) {
                    bestFreq = p.second;
                    bestKey = p.first;
                }
            }
            result.push_back(bestKey);
            freq.erase(bestKey);
        }
        return result;
    }
};