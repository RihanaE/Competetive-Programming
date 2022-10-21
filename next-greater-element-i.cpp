class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> stack;
        unordered_map<int,int> dict;
        for(int i = 0; i < nums2.size(); i++){
            if(i == 0 || stack.back() > nums2[i]){
                stack.push_back(nums2[i]);
            }
            else{
                while(stack.size()>0 && stack.back() < nums2[i]){
                    dict[stack.back()] = nums2[i];
                    stack.pop_back();
                }
                stack.push_back(nums2[i]);
            }
        }
        stack.clear();
        for(int i: nums1){
            if(dict[i] != 0)
                stack.push_back(dict[i]);
            else
                stack.push_back(-1);
        }
        return stack;
            
        
    }
};
