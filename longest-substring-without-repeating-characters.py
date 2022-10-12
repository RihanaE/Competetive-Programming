class Solution(object):
    def isValid(self, s):
        for i in range(len(s)):
            for j in range(i + 1, (i + 100 if i +100 < len(s) else len(s))):
                if s[i] == s[j]:
                    return False
        return True
    def lengthOfLongestSubstring(self, s):
        Max = 1
        if(len(s)<1000):
            for i in range(len(s)-1):
                count = 1
                for j in range(i+1, (len(s) if len(s) < i + 94 else i + 94 )):
                    if Solution.isValid(self, s[i:j+1]):
                        count+=1
                    else: 
                        break
                if Max < count:
                    Max = count
            return Max if len(s)>0 else 0
        else:
            return 95
    
    

        
