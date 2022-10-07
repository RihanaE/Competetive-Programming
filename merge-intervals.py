class Solution(object):
    def merge(self, intervals):
        i = 0
        j = i+1
        self.sort(intervals)
        while i < len(intervals)-1:
            if intervals[i][0] == intervals[i+1][0]:
                if intervals[i][1] >= intervals[i+1][1]:
                    del intervals[i+1]
                else:
                    del intervals[i]
            else:
                if intervals[i][1] >= intervals[i+1][1]:
                    del intervals[i+1]
                else:
                    if intervals[i][1] < intervals[i+1][0]:
                        i+=1
                    else:
                        intervals[i][1] = intervals[i+1][1]
                        del intervals[i+1]
        return intervals
    def sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            
            self.sort(L)
            self.sort(R)
            
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][0] <= R[j][0]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1
            while i < len(L):
                arr[k] = L[i]
                k+=1
                i+=1
            while j < len(R):
                arr[k] = R[j]
                k+=1
                j+=1
