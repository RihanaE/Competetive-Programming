class Solution(object):
    def kClosest(self, points, k):
        self.Sort(points)
        return points[:k]
    def dist(self, p):
        return p[0]**2 + p[1]**2
    def Sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.Sort(L)
            self.Sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if self.dist(L[i]) <= self.dist(R[j]):
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
    

        
