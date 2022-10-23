class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        count = 0
        i = 0
        temp = Counter(nums)
        j = len(nums)-1
        while i < j:
            if nums[i] != nums[j]:
                if nums[i] + nums[j] == k:
                    jump = min([temp[nums[i]], temp[nums[j]]])
                    count = count + jump
                    temp[nums[i]] -= jump
                    temp[nums[j]] -= jump
                    i+=jump
                    j-=jump
                    
                elif nums[i] + nums[j] > k:

                    j-=temp[nums[j]]
                else:
                    i+= temp[nums[i]]
            else:
                if nums[i]*2 == k:
                    count+=(j-i+1)//2
                return count
        return count
        
