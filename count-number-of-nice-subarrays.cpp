class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        nums.insert(nums.begin(), 0);
        int count = 0;
        for(int i = 1;i < nums.size(); i++){
            nums[i] = (nums[i]%2 + nums[i-1]);
            if(nums[i] == k)
                count++;
            if(freq.find(nums[i] - k)!= freq.end())
                count+=freq[nums[i]-k]; 
            if(freq.find(nums[i])!= freq.end())
                freq[nums[i]] +=1;
            else
                freq[nums[i]] = 1;
            
        }
        
        return count;
    }
};
