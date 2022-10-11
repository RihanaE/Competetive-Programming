class Solution(object):
    def numRescueBoats(self, people, limit):
        self.Sort(people)
        i = count = 0
        j = len(people)-1
        while i < j:
            if people[i] + people[j] > limit:
                j-=1
            else:
                i+=1
                j-=1
            count+=1
        if i == j:
            count+=1
        return count
                
               
        
 
    def Sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.Sort(L)
            self.Sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
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
        
