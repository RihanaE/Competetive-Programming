import operator
from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        sum = count = 0
        freq = self.sort_dict(Counter(arr))
        for i in freq:
            count+=1
            sum+= i[1]
            if sum >= len(arr)/2:
                return count
        return count
    def sort_dict(self, book):
        li  = book.items()
        self.Sort(li)
        return li
    
    def Sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.Sort(L)
            self.Sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][1] >= R[j][1]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    
