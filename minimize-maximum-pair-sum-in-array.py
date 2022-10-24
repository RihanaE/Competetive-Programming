class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        sum = 0
        for i in range(len(nums)/2):
            if nums[i] + nums[-i - 1] > sum:
                sum = nums[i] + nums[-i - 1]
        return sum
