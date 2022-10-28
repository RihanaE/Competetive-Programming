class Solution(object):
    def validateStackSequences(self, pushed, popped):
        arr = []
        i = j = 0
        while i < len(pushed):
            if not arr or arr[-1] != popped[j]:
                arr.append(pushed[i])
                i+=1
            while arr and arr[-1] == popped[j] and j < len(popped):
                arr.pop()
                j+=1
        return not bool(len(popped) - j)
