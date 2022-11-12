class Solution(object):
    #define a variable that signals the loop to halt when all parking functions are iterated through
    def __init__(self):
        self.toggle = 1 

    def generateParenthesis(self, n):
        counter, braks = n*[0],[]
        #toggle = 1 until counter goes through every parking function
        while self.toggle:
            i, s = 1, "()"
            # chech the entries of counter
            while i < n:
                #insert () according with the change in value of counter[i]
                s = s[:i + counter[i]] + "()" + s[i + counter[i]:]
                i+=1
            braks.append(s)
            #"increse" counter by 1
            counter = self.incr(counter)
        return braks

    def incr(self, c):
        if  c[-1] + 1 < len(c):
            c[-1]+=1
        elif len(c) == 1:
            self.toggle = 0
            return c
        else:
            c = self.incr(c[:-1])
            c.append(c[-1])
        return c
"""
counter goes like: [0,0, ... ,0,0]
                   [0,0, ... ,0,1]
                   [0,0, ... ,1,1] 
                        .
                        .
                        .
                   [0,1, ..., n-2, n-1]
"""
