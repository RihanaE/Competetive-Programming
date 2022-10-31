class Solution {
    public int lengthOfLongestSubstring(String s) {
        int mx = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        
        int i = 0;
        for(int j=0; j < s.length(); j++){
            char c = s.charAt(j);

            if(map.containsKey(c) && map.get(c) >= i)
                i = map.get(c) + 1;
			int wind = j-i+1;
            mx = Math.max(wind, mx);
            map.put(c, j);            
        }
        return mx;
    }
}
