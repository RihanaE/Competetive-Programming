class Solution(object):
    def removeKdigits(self, num, k):
        mono = []
        for i in xrange(len(num)):
            while mono and k and mono[-1] > num[i]:
                mono.pop()
                k-=1
            mono.append(num[i])
            i+=1
        ans = str(int("".join(mono)))[:-k] if k else str(int("".join(mono)))
        return ans if len(ans) else "0"
            
        
