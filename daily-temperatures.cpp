class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> waits, mono;        
        for(int i = 0; i < temperatures.size(); i++){
            if(i == 0 || temperatures[mono[mono.size()-1]] >= temperatures[i]){
            
            }
            else{
                int j = 1, k = 0;
                while(mono.size() > 0 && temperatures[mono[mono.size()-1]] < temperatures[i]){
                    waits[mono[mono.size()-1]] = i - mono[mono.size()-1];
                    mono.pop_back();
                }
                    
            }
            mono.push_back(i);
            waits.push_back(0);   
        }
        return waits;
    }
};
