class Solution(object):
    def garbageCollection(self, garbage, travel): 
        i = 0
        gar = {'M':0, 'G':0, 'P':0}
        gar_ref = {'M':0, 'G':0, 'P':0}
        trav = [0]
        blocks = [[],[],[]]
        m = p = g = 0
        while i < len(garbage):
            j = 0
            while j < len(garbage[i]):
                gar_ref[garbage[i][j]]+=1
                j+=1
            if gar_ref['M'] - gar['M']:
                blocks[0].append(i)
                gar['M'] = gar_ref['M']
            if gar_ref['G'] - gar['G']:
                blocks[1].append(i)
                gar['G'] = gar_ref['G']
            if gar_ref['P'] - gar['P']:
                blocks[2].append(i)
                gar['P'] = gar_ref['P']
            if i < len(travel):
                trav.append(travel[i] + trav[i])
            else:
                print(blocks)
            i+=1
        i = 0
        m = gar['M'] + trav[blocks[0][-1]] if blocks[0] else gar['M']
        g = gar['G'] + trav[blocks[1][-1]] if blocks[1] else gar['G']
        p = gar['P'] + trav[blocks[2][-1]] if blocks[2] else gar['P']
        

        return m+p+g
