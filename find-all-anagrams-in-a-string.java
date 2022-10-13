class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> indices = new ArrayList<Integer>();
        if(p.length() > s.length())
            return indices;
        else{
            HashMap<Character, Integer> pmap, smap;
            pmap =  new  HashMap<Character, Integer>();
            for(int i = 0; i < p.length(); i++){
                pmap.put(p.charAt(i), pmap.getOrDefault(p.charAt(i), 0) + 1 );
            }
            int i = 0;
            int j = i + p.length();
            for(int k = i ; k < j; k++){
                if(pmap.containsKey(s.charAt(k)))
                    pmap.put(s.charAt(k), pmap.get(s.charAt(k)) - 1);
            }
            if(isZero(pmap))
                    indices.add(i);
            
            while(j < s.length()){
                if(pmap.containsKey(s.charAt(i)))
                    pmap.put(s.charAt(i), pmap.get(s.charAt(i)) + 1);
                if(pmap.containsKey(s.charAt(j)))
                    pmap.put(s.charAt(j), pmap.get(s.charAt(j)) - 1);
                i++;
                j++;
                if(isZero(pmap))
                    indices.add(i);
                
            }
            return indices;
        }
        
        
        
    }
    public boolean isZero(HashMap<Character, Integer> pmap){
        for(int val:pmap.values())
            if(val != 0)
                return false;
        return true;
    }
}
