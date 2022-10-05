class Solution {
public:
    void sortColors(vector<int>& nums) {
      
/**        int temp; // using selecting sort algorithm (O(nlog(n)) time complexity;  100% faster of all C++ submissions
           for(int i = 0; i < nums.size(); i++){
               for (int j = i; j< nums.size();j++){
                   if(nums[j]<nums[i]){
                       temp = nums[i];
                       nums[i] = nums[j];
                        nums[j] = temp;
                   }               
               }        
*/         }
      
        int i = 0, j = 0; // ROUGHLY one-pass (O(n) complexity) algorithm; 
        while(j < nums.size()){
            if(nums[i] == 1){
                i++;}
            else if (nums[i] == 0){
                nums.erase(nums.begin() + i);
                nums.insert(nums.begin(), 0);
                i++;
            }
                
            else{
                nums.erase(nums.begin() + i);
                nums.insert(nums.end(), 2);

            }
            j++;
        }
    }
};
