class Solution(object):
    def rotate(self, nums, k):
        nums1  = nums[(-k)%len(nums):]
        nums2 = nums[:(-k)%len(nums)]
        return nums1 + nums2
