class Solution {
public:
    int sum(vector<int> &nums, int i, int j){
        int s = 0;
        while(i < j)
            s = s + nums[i++];
        return s;
            
    }

    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int i = 0, j = firstLen, k = firstLen, l = firstLen + secondLen;
        int firstSum = sum(nums, i, j), secondSum = sum(nums, k, l);
        int maxSum = 0;
        while(j <= nums.size()){
            k = 0;
            l = secondLen;
            secondSum = sum(nums, k, l);
            while(l <= nums.size() ){
                if((i >= l || j <= k) && firstSum + secondSum > maxSum)
                    maxSum = firstSum + secondSum;
                k++;
                l++;
                if(l-1 < nums.size())
                    secondSum = secondSum - nums[k-1] + nums[l-1];
            }
            i++;
            j++;
            if(j-1 < nums.size())
                firstSum =  firstSum - nums[i-1] + nums[j-1];
            
        }
        
        
        return maxSum;
        
    }
};
