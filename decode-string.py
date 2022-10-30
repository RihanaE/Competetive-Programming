class Solution(object):
    def decodeString(self, s):
        if not "[" in s:
            return s
        else:
            for i, c in enumerate(s):
                if c == '[':
                    l = i
                if c == ']':
                    r = i
                    break
            n = ""
            j = l-1
            while ord(s[j]) < 60 and j > -1:
                n = s[j]+ n
                j-=1
            s = s[:j+1] + int(n)*s[l+1:r] + s[r+1:]
            return self.decodeString(s)     
