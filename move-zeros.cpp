class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = 1;
        int temp;
        for(; j < nums.size(); ){
            if(nums[i] == 0 && nums[j] != 0){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j++;
            }
            else if((nums[i] == 0 && nums[j] == 0) || i == j){
                j++;   
            }
            else if(nums[i] != 0 && nums[j] == 0)
                i++;
            else{
                i++;
                j++;
                    
            }
                
        }
    }
};
