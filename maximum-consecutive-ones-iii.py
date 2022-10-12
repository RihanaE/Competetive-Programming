class Solution(object):
    def longestOnes(self, nums, k):
        i = 0
        j = k
        extra = 0
        ones = len(list(filter(lambda x: x == 1, nums[i:j])))
        max_sum  = k
        while j < len(nums):
            if (nums[j] == 0) and j - i - ones + 1 <= k:
                max_sum+=1
                j+=1
            elif nums[j] == 0 and nums[i] == 1 and j - i - ones + 1 > k:
                i+=1
                j+=1
                extra +=1
                while j < len(nums) and extra > 0:
                    if(nums[i] == 1 and nums[j] == 0):
                        extra+=1
                    elif nums[i] == 0 and nums[j] == 1:
                        extra-=1
                    j+=1
                    i+=1
 
            elif nums[j] == 0 and nums[i] == 0 and j - i - ones + 1 > k:
                i+=1
                j+=1
            elif nums[j] == 1:
                max_sum+=1
                ones+=1
                j+=1
        return max_sum
