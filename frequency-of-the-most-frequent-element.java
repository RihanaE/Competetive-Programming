class Solution {
    	public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int i = 0, j = 0, sum = 0, max = 0;
        for (i=0;i<nums.length;i++){
            sum += nums[i];
            while (nums[i] * (i - j + 1) - sum > k){ sum -= nums[j++];}
            max = Math.max(max_val,i-j+1);
        }
        return max_val;
    }
}
