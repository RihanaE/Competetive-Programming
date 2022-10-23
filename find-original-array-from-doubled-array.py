class Solution(object):
    def findOriginalArray(self, changed):
        changed.sort()
        res = []
        strt = 0 
        temp = Counter(changed)
        
        if len(changed)%2:
            return []
        else:
            for i in changed:
                if not temp[i]:
                    continue
                else:
                    if temp.get(2*i, 0):
                        res.append(i)
                        temp[2*i]-=1
                        temp[i]-=1
                    else:
                        return []
        return res

    
            
        
                
        
