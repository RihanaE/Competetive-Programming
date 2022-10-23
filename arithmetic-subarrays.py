class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        answer = []
        for i in range(len(l)):
            answer.append(self.isArithmetic(nums[l[i]:r[i]+1]))
        return answer
    def isArithmetic(self, nums):
        nums.sort()
        d = nums[1] - nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != d:
                return False
        return True
            
        
        
        
