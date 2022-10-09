class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        nums.insert(nums.begin(), 0);
        for(int i = 1;i < nums.size(); i++){
                nums[i] = nums[i] + nums[i-1];
        }
        int left, right;
        for(int i = 1; i < nums.size(); i++){
            left = nums[i-1];
            right = nums[nums.size()-1] -  nums[i];
            if(left ==  right)
                return i-1;
            
        }
        return -1;
    }
};
