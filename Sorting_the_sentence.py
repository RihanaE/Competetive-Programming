class Solution(object):
    def sortSentence(self, s):
        arr  = s.split(" ")
        sort =[]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if int(arr[j][len(arr[j]) - 1]) == (i+1):
                    sort.append(arr[j][:(len(arr[j])-1)])
        return " ".join(sort)
        
