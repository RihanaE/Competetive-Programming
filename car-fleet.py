class Solution(object):
    def carFleet(self, target, pos, s):
        time = [float((target - p)/s) for p,s in sorted(zip(pos, s))]
        stack = []
        for i in time:
            while stack and stack[-1] <= i:
                stack.pop()
            stack.append(i)
        return len(stack)
