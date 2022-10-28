class Solution(object):
    def longestSubarray(self, nums, limit):
        i = 0
        ans = 1
        queue = []
        for j in range(len(nums)):
            bisect.insort(queue, nums[j])
            if queue[-1] - queue[0] > limit:
                queue.pop(bisect.bisect(queue, nums[i]) - 1)
                i += 1
            ans = max(ans, j - i + 1)
        return ans
