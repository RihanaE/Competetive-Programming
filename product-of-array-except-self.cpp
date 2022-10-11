class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left, right, answer;
        left.push_back(1);
        right.push_back(1);
        for(int i = 0; i < nums.size()-1; i++){
            left.push_back(nums[i] * left[left.size()-1]);
            right.push_back(right[right.size()-1] * nums[nums.size()-i-1]);
        }
        for(int i =0; i < nums.size(); i++)
            answer.push_back(left[i]*right[nums.size()-1-i]);
    
        return answer;
        
        
    }
};
