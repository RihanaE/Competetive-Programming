class Solution(object):
    def hIndex(self, c):
        c.sort()
        c.reverse()
        i = 0
        h = [i for i in range(c[0]+1)]
        for cit in h[::-1]:
            j = 0
            while j < len(c) and c[j]-cit >= 0 and cit:
                j+=1
                i = j
                if j == cit:
                    return j
        return i
                
                
