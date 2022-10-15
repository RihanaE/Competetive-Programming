class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        
        return sort(nums)[k-1];
        
    }
    public String[] sort(String[] arr){
        if(arr.length > 1){
            int mid =  arr.length/2;
            String[] L =  new String[mid];
            String[] R = new String[arr.length-mid];

            for(int i = 0; i < mid; i++){
                L[i] = arr[i];
                R[i] = arr[i + mid];
            }
            if(arr.length % 2 == 1)
                R[R.length - 1] = arr[arr.length - 1];
            
            L = sort(L);
            R = sort(R);
            
            int i = 0, j = 0, k = 0;
            
            while(i < L.length && j < R.length){
                if(compareInt(L[i], R[j])){
                    arr[k] = L[i];
                    i++;
                }
                else{
                    arr[k] = R[j];
                    j++;
                }
                k++;
            }
            while(i < L.length){
                arr[k] = L[i];
                k++;
                i++;
            }
            while(j < R.length){
                arr[k] = R[j];
                k++;
                j++;
            }
            
        }
        return arr;
        
    }
    public boolean compareInt(String s, String p){
        if(s.length() > p.length())
            return true;
        else if (s.length() < p.length())
            return false;
        else{
            if (s.compareTo(p) >= 0)
                return true;
            else
                return false;
        }
        
    }
 }
