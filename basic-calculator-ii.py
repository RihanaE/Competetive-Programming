class Solution(object):
    def calculate(self, s):
        t = s.replace("-", "+-")
        arr = t.split("+")
        print(int(-1/2))
        r =0
        for i in arr:
            r+=self.evaluate(i)
        return int(r)
        
    def evaluate(self, s):
        t = ""
        tint = 1
        prev = "*"
        i = 0
        while i < len(s):
            if s[i] != "*" and s[i] != "/":
                t+=s[i]
                
            else: 
                if prev == "*":
                    tint = tint*int(t)
                else:
                    tint = int(1.0*tint/int(t))
                prev = s[i]
                t = ""
            i+=1
        if prev == "*":
            return tint*int(t)
        else:
            return int(1.0*tint/int(t))
