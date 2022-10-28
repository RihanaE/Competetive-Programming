class Solution(object):
    def maxArea(self, height):
        area = 0
        n = len(height)
        i, j = 0,len(height)-1
        while i < j:
            area = max(abs(j-i)*min(height[j], height[i]), area)
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return area
