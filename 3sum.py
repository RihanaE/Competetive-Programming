class Solution(object):
    def threeSum(self, nums):
        dic = Counter(nums)
        mn, mx, ans =  min(dic.keys()), max(dic.keys()), []
        keys = sorted(dic.keys())
        i = 0
        while  i < len(keys):
            j = i
            dic[keys[i]]-=1
            while j < len(keys):
                dic[keys[j]]-=1
                if dic[keys[i]] >= 0  and dic[keys[j]] >= 0 and dic.get(-keys[i]-keys[j], 0) > 0:
                    if keys[i] <= keys[j] <= -keys[i]-keys[j]:
                        ans.append([keys[i], keys[j], -keys[i]-keys[j]])
                dic[keys[j]]+=1
                j+=1
            dic[keys[i]]+=1
            i+=1
        return ans
