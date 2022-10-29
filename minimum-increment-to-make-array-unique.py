class Solution(object):
    def minIncrementForUnique(self, nums):
        ans = inc  = 0
        nums.sort()
        for i in nums:
            ans += max(inc - i, 0)
            inc = max(inc + 1, i + 1)
        return ans
