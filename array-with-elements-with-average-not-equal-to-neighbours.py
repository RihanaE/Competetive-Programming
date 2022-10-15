class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        mid = int((len(nums)+1)/2)
        L = nums[: mid]
        R =  nums[mid:]
        arr = []
        for i in range(mid):
                arr.append(nums[i])
                i+=1
                arr.append(nums[len(nums)-i])
        if len(nums)%2 == 1:
            arr.pop()
        return arr
            
        
