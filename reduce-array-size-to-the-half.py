import operator
from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        sum = count = 0
        freq = Counter(arr)
        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse = True))
        for i in freq.keys():
            count+=1
            sum+= freq[i]
            if sum >= len(arr)/2:
                return count
        return count
